import grpc

from grpc_logger_pb2_grpc import LogServiceStub
from grpc_logger_pb2 import WriteLogRequest, WriteLogResponse, LogMessage, LogAgenda, LogLevel


class GrpcWriteLogFailed(Exception):
    pass


class TestClientGrpcWriteLog(object):
    def __init__(self):
        #TODO change to config
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def setup_stubs(self):
        self.log_service_stub = LogServiceStub(self.channel)

    # write log via gRPC stub do remote Mongo DB
    def grpc_write_log(self, agenda: LogAgenda, level: LogLevel, message: str) -> WriteLogResponse:
        request = WriteLogRequest(
            log=LogMessage(agenda=agenda, level=level, message=message)

        )
        return self.log_service_stub.WriteLog(request)


if __name__ == "__main__":
    try:
        # prepare log object fields
        # log object fileds shoud be  inside try clausule as to catch variable
        # type errors checked by grpc stub
        agenda = LogAgenda.DEFAULT
        level = LogLevel.LOG_LEVEL_WARNING
        message = "Testing log message"
        
        client = TestClientGrpcWriteLog()

        response: WriteLogResponse = client.grpc_write_log(
            agenda, level, message)

        # ivalid response from grpc host
        if response.status != WriteLogResponse.STATUS_OK:
            raise GrpcWriteLogFailed(response.message)

    except Exception as e:
        print(e)
