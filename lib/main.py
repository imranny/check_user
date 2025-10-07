import asyncio
import logging
from workers.worker import Worker
from schemas.database import create_tables, delete_tables

logging.basicConfig(level=logging.INFO)


async def main():
    await create_tables()
    worker = Worker()
    await worker.run_stage_to_done()


if __name__ == "__main__":
    asyncio.run(main())