import signal
from concurrent import futures

import grpc
from grpc_logger_pb2_grpc import add_LogServiceServicer_to_server
from servicers.grpc_logger import WriteLogServicer

GRPC_MAX_WORKERS = 10
GRPC_INSECURE_PORT = 50050
GRPC_SECURE_PORT = 50051


class Server(object):
    def __init__(self):
        self._create_server()
        self._add_servicers()

    def _create_server(self):
        self._server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=GRPC_MAX_WORKERS),
            options=self._server_options(),
        )

    def _server_options(self):
        server_options = (
            # send keepalive every x milliseconds
            ("grpc.keepalive_time_ms", 20000),
            (
                "grpc.keepalive_timeout_ms",
                5000,
            ),  # keepalive ping time out after x milliseconds
            (
                "grpc.keepalive_permit_without_calls",
                True,
            ),  # allow keepalive pings when there's no gRPC calls
            (
                "grpc.http2.max_pings_without_data",
                0,
            ),  # allow unlimited amount of keepalive pings without data
            (
                "grpc.http2.min_time_between_pings_ms",
                10000,
            ),  # allow grpc pings from client every x milliseconds
            (
                "grpc.http2.min_ping_interval_without_data_ms",
                5000,
            ),  # allow grpc pings from client without data every x milliseconds
        )
        return server_options

    def _add_servicers(self):
        add_LogServiceServicer_to_server(WriteLogServicer(), self._server)

    def setup_insecure_server(self):
        self._server.add_insecure_port(
            "[::]:{insecure_port}".format(insecure_port=GRPC_INSECURE_PORT)
        )

    def serve(self):
        print("Server running....")
        self._server.start()
        self._server.wait_for_termination()


def handle_sigterm(*args):
    raise KeyboardInterrupt()


signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    server = Server()
    server.setup_insecure_server()
    server.serve()
