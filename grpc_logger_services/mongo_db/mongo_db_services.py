# Writes log data to Mongo DB using
import motor
from beanie import init_beanie
from mongo_db.mongo_db_models import LogsDocument
from config.config import settings


# Beanie is fully asynchronous, so we will access it from an async function
async def init_db():
    # Beanie uses Motor under the hood
    _mongo_url = f'{settings.MONGO_HOST}:{settings.MONGO_PORT}'
    client = motor.motor_asyncio.AsyncIOMotorClient(_mongo_url)

    # Init beanie with the Product document class
    await init_beanie(database=client.logs, document_models=[LogsDocument])
