from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///users.db"
)

new_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Model(DeclarativeBase):
    pass

class UsersDB(Model):
    __tablename__= 'users'

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    age: Mapped[int]
    sex: Mapped[Optional[str]]
    job: Mapped[Optional[str]]

async def create_tables():

    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():

    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

