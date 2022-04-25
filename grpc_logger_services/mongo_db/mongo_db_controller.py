# Writes log data to Mongo DB using

from mongo_db.mongo_db_models import LogDbModel

#write log message do Mongo DB
def write_log_to_db(model : LogDbModel ) -> None:
    print(model)

