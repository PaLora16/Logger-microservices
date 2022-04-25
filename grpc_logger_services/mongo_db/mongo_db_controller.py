# Writes log data to Mongo DB using

from mongo_db.mongo_db_models import LogDbModel
def write_log_to_mongo_db(model : LogDbModel ):
    print(model)