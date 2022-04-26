# Writes log data to Mongo DB using

import  motor
from beanie import  init_beanie
from mongo_db.mongo_db_models import LogsDocument

    
# Beanie is fully asynchronous, so we will access it from an async function
async def init_db():
    # Beanie uses Motor under the hood 
    #TODO Here use values from configuration
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
 
    # Init beanie with the Product document class
    await init_beanie(database=client.logs, document_models=[LogsDocument])

