# from . import service_method
# from logger import module_logger
from grpc_logger_pb2_grpc import LogServiceServicer as grpc_LogServiceServicer
from grpc_logger_pb2 import WriteLogResponse


class WriteLogServicer(grpc_LogServiceServicer):
    # def __init__(self):
    #     self.logger = module_logger(__name__)

    # @service_method(logging=False)
    def WriteLog(self, request, context):
        """
        Check connections to the service's dependencies, reporting the status:
            - database
            - file store
            - caching layer
            - queuing system
            - external logger
            - etc.
        """
        # return WriteLogResponse(status_code=LogRequestStatus.STATUS_OK)
        return WriteLogResponse(status = "Response super OK")
