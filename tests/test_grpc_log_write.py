import time
import grpc

from grpc_logger_pb2_grpc import LogServiceStub
from grpc_logger_pb2 import WriteLogRequest, LogMessage, LogAgenda, LogLevel, ResponseStatus


class TestClientGrpcWriteLog(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def setup_stubs(self):
        self.log_service_stub = LogServiceStub(self.channel)

    def write_log(self):
        request = WriteLogRequest(
            log=LogMessage(
                agenda=LogAgenda.DEFAULT,
                level=LogLevel.LOG_LEVEL_ERROR,
                message="Another log"
            )

        )
        
    def write_log_bad_format(self):
        request = WriteLogRequest(
            log=LogMessage(
                agenda=LogAgenda.HEALTH_CHECK,
                level=LogLevel.LOG_LEVEL_CRITICAL,
                message="Another log so far"
            )

        )        
        return self.log_service_stub.WriteLog(request)


if __name__ == "__main__":
    write_log_client = TestClientGrpcWriteLog()
    response = write_log_client. write_log_bad_format()
   
    if (response.status == ResponseStatus.STATUS_OK):
        print(f"Returned value : {response.message}")
