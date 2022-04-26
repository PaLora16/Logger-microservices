import grpc

from grpc_logger_pb2_grpc import LogServiceStub
from grpc_logger_pb2 import WriteLogRequest, WriteLogResponse, LogMessage, LogAgenda, LogLevel


class TestClientGrpcWriteLog(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def setup_stubs(self):
        self.log_service_stub = LogServiceStub(self.channel)

    def get_log_response(self):
        request = WriteLogRequest(
            log=LogMessage(
                agenda=LogAgenda.DEFAULT,
                level=LogLevel.LOG_LEVEL_ERROR,
                message="Another LOg form client"
            )

        )
        return self.log_service_stub.WriteLog(request)


if __name__ == "__main__":
    client = TestClientGrpcWriteLog()
    response = client.get_log_response()
    # print(f"Response from server {response.message}")
    print(response)
