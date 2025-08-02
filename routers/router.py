from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from dto import User, UserResponse
from databases.database import new_session, UsersDB
from sqlalchemy import select

router = APIRouter()


@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(User):
    async with new_session() as session:
        result = await session.execute(select(UsersDB).where(UsersDB.id == User.id))
        user_db = result.scalar_one_or_none()

        if not user_db:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "success": True,
            "user": User(
                id=user_db.id,
                name=user_db.name,
                age=user_db.age,
                job=user_db.job
            )
        }


@router.post("/user", response_model=UserResponse)
async def create_user(user: Annotated[User, Depends()]):
    async with new_session() as session:
        user_db = UsersDB(
            id=user.id,
            name=user.name,
            age=user.age,
            job=user.job
        )
        session.add(user_db)
        await session.commit()

        return {
            "success": True,
            "user": user
        }




