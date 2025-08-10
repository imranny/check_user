from typing import Optional, Literal
from sqlalchemy import String
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import engine



new_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Model(DeclarativeBase):
    pass

class UsersDB(Model):
    __abstract__= True

    id: Mapped[int] = mapped_column(primary_key= True, autoincrement=True)
    name: Mapped[str]
    age: Mapped[int]
    sex: Mapped[Optional[str]]
    job: Mapped[Optional[str]]

class UsersStageDB(UsersDB):
    __tablename__ = 'users_stage'

class UsersDoneDB(UsersDB):
    __tablename__ = 'users_done'
    age_class: Mapped[Literal["child", "adolescent", "adult"]] = mapped_column(String(10))

async def create_tables():

    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():

    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

