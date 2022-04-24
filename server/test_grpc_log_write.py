import time

# from socket import gethostname, gethostbyname

import grpc

import grpc_logger_pb2_grpc
from grpc_logger_pb2 import WriteLogResponse, WriteLogRequest


class TestClientGrpcWriteLog(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def setup_stubs(self):
        self.log_service_stub = grpc_logger_pb2_grpc.LogServiceStub(self.channel)

    def get_log_response(self):
        # hostname = gethostname()
        # ip_addr = gethostbyname(hostname)
        # response = self.system_info_stub.SystemInfo(
        #     SystemInfoRequest(
        #         client_info=ClientInfo(
        #             host_info=HostInfo(
        #                 hostname=hostname,
        #                 ip_addr=ip_addr,
        #                 port=50050,
        #                 timestamp=int(time.time()),
        #             )
        #         )
        #     )
        # )
        response = self.log_service_stub(WriteLogRequest())
        return response


if __name__ == "__main__":
    client = TestClientGrpcWriteLog()
    print(client.get_log_response())
