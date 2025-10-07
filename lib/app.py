
from fastapi import FastAPI
from routers.router import router
from schemas.database import create_tables

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await create_tables()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)