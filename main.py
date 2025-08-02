from fastapi import FastAPI
from routers.router import router
from databases.database import create_tables
from contextlib import asynccontextmanager
import uvicorn

app = FastAPI()
app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)


app = FastAPI(lifespan=lifespan)