from grpc_logger_pb2_grpc import LogServiceServicer as grpc_LogServiceServicer
from grpc_logger_pb2 import WriteLogResponse, WriteLogRequest, ResponseStatus


class WriteLogServicer(grpc_LogServiceServicer):
    def WriteLog(self, request : WriteLogRequest, context):
        return WriteLogResponse(status=ResponseStatus.STATUS_UNSPECIFIED_ERROR , message = "BAD BAD")