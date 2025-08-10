import logging
from clients.client import Client

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self):
        self.client = Client()

    async def run_stage_to_done(self) -> None:
        logger.info("Starting worker")

        await self.client.export_users_to_json()

        success = await self.client.move_stage_to_done()

        if success:
            logger.info("Successfully moved all users from stage to done")
        else:
            logger.error("Failed to move users from stage to done")