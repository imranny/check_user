from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.database import UsersStageDB, UsersDoneDB
import logging

logger = logging.getLogger(__name__)


async def check_user_exists(session: AsyncSession, user_data: dict) -> bool:
    result = await session.execute(
        select(UsersStageDB).where(
            UsersStageDB.name == user_data["name"],
            UsersStageDB.age == user_data["age"],
            UsersStageDB.sex == user_data["sex"],
            UsersStageDB.job == user_data["job"]
        )
    )
    return result.scalar_one_or_none() is not None


