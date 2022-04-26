# Writes log data to Mongo DB using

import asyncio
from mongo_db.mongo_db_models import LogsDocument
from grpc_logger_pb2 import WriteLogRequest
from mongo_db.mongo_db_services import init_db
from datetime import datetime




# write log message do Mongo DB
# def write_log_to_db(request: WriteLogRequest) -> None:
#     print(request)

# Beanie is fully asynchronous, so we will access it from an async function
async def write_log_to_db(request: WriteLogRequest) -> None:
    print(request)
    # asyncio.run(init_db())
    await init_db()        
    _log = LogsDocument(
        agenda=request.log.agenda, level=request.log.level, message=request.log.message, timestamp = datetime.now())
    await _log.insert()
    # chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
    # # Beanie documents work just like pydantic models
    # tonybar = Product(name="Tony's", price=5.95, category=chocolate)
    # # And can be inserted into the database
    # await tonybar.insert()

    # # You can find documents with pythonic syntax
    # product = await Product.find_one(Product.price < 10)

    # And update them
    # await product.set({Product.name:"Gold bar"})

# if __name__ == '__main__':
#     request = WriteLogRequest(
#         log=LogMessage(
#             agenda=LogAgenda.DEFAULT,
#             level=LogLevel.LOG_LEVEL_ERROR,
#             message="Please log my error"
#         )

#     )    
#     asyncio.run(write_log_to_db(request))
