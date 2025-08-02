from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from lib.dto import User, UserResponse
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

        return UserResponse(
            success = True,
            user = user_db
        )


@router.post("/user", response_model=UserResponse)
async def create_user(user: Annotated[User, Depends()]):
    async with new_session() as session:
        if user.id:
            existing_user = await session.get(UsersDB, user.id)
            if existing_user:
                raise HTTPException(status_code=400, detail="User already exists")


        user_db = UsersDB(**user.model_dump())

        session.add(user_db)
        await session.commit()

        return UserResponse(
            success = True,
            user = user_db
        )




