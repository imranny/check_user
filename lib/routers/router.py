from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from schemas.dto import UserCreate, UserReturn, UserResponse
from schemas.database import new_session, UsersStageDB
from utils.utils import check_user_exists

router = APIRouter()


@router.post("/user", response_model=UserResponse)
async def create_user(user: Annotated[UserCreate, Depends()]):
    async with new_session() as session:

        user_dict = user.model_dump()
        if await check_user_exists(session, user_dict):
            raise HTTPException(status_code=400, detail="User already exists")

        user_db = UsersStageDB(**user.model_dump())

        session.add(user_db)
        await session.commit()
        await session.refresh(user_db)

        user_data = {
            "id": user_db.id,
            "name": user_db.name,
            "age": user_db.age,
            "sex": user_db.sex,
            "job": user_db.job
        }
        return UserResponse(success=True, user=user_data)

@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    async with new_session() as session:
        user_db = await session.get(UsersStageDB, user_id)

        if not user_db:
            raise HTTPException(status_code=404, detail="User not found")

        return UserResponse(success=True, user=UserReturn(**user_db.__dict__))


@router.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    async with new_session() as session:
        user_db = await session.get(UsersStageDB, user_id)

        if not user_db:
            raise HTTPException(status_code=404, detail="User not found")

        await session.delete(user_db)
        await session.commit()

        return {"success": True, "message": "User deleted"}



