import json
import logging
from typing import List
from schemas.database import new_session, UsersStageDB, UsersDoneDB
from sqlalchemy import select
from processors.processor import user_to_json


logger = logging.getLogger(__name__)


class Client:

    def __init__(self, session_maker=new_session):
        self.session_maker = session_maker


    async def get_all_users(self) -> List[UsersStageDB]:
        async with self.session_maker() as session:
            result = await session.execute(select(UsersStageDB))
            return result.scalars().all()

    async def export_users_to_json(self, output_file: str = "users_json.json") -> bool:
        try:
            users = await self.get_all_users()
            users_data = [user_to_json(user) for user in users]

            with open(output_file, "w") as f:
                json.dump(users_data, f, indent=4, ensure_ascii=False)
            return True

        except Exception as e:
            logger.error(f"Error exporting users info: {e}")
            return False


    async def move_stage_to_done(self) -> bool:
        try:
            async with new_session() as session:
                result = await session.execute(select(UsersStageDB))
                stage_users = result.scalars().all()

                for user in stage_users:
                    user_data = user_to_json(user)

                    done_user = UsersDoneDB(
                        name=user_data["name"],
                        age=user_data["age"],
                        sex=user_data["sex"],
                        job=user_data["job"],
                        age_class=user_data["age_class"]
                    )
                    session.add(done_user)

                    await session.delete(user)

                await session.commit()
                return True

        except Exception as e:
            logger.error(f"Error moving users to done: {e}")
            return False