from grpc_logger_pb2_grpc import LogServiceServicer as grpc_LogServiceServicer
from grpc_logger_pb2 import WriteLogResponse, WriteLogRequest, ResponseStatus
from mongo_db.mongo_db_models import LogDbModel
from mongo_db.mongo_db_controller import write_log_to_mongo_db


class WriteLogServicer(grpc_LogServiceServicer):
    def WriteLog(self, request : WriteLogRequest, context):
        model = LogDbModel(request.log.agenda, request.log.level, request.log.message)
        write_log_to_mongo_db(model)
        return WriteLogResponse(status=ResponseStatus.STATUS_UNSPECIFIED_ERROR , message =str(request.log.level))