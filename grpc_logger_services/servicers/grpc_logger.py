from grpc_logger_pb2_grpc import LogServiceServicer as grpc_LogServiceServicer
from grpc_logger_pb2 import WriteLogResponse


class WriteLogServicer(grpc_LogServiceServicer):
    def WriteLog(self, request, context):
        return WriteLogResponse(status="Response super OK")
