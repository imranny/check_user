import os
from sqlalchemy.ext.asyncio import create_async_engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "users.db")


engine = create_async_engine(f"sqlite+aiosqlite:///{DB_PATH}")