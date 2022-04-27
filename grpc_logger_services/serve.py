# Main loop listening for clients requests and
import signal
from concurrent import futures
import grpc

from grpc_logger_pb2_grpc import add_LogServiceServicer_to_server
from servicers.grpc_logger import WriteLogServicer
from config.config import settings


# Sever configuration constants
# Relatively unmutable. Next enhancement can move constants into congfig fields
KEEPALIVE_TIME_MS = 20000
KEEPALIVE_TIMEOUT_MS = 5000
KEEPALIVE_PERMIT_WITHOUT_CALLS = True
MAX_PINGS_WITHOUT_DATA = 0
MIN_TIME_BETWEEN_PINGS_MS = 10000
MIN_PING_INTERVAL_WITHOUT_DATA_MS = 5000


class Server(object):
    def __init__(self):
        self._create_server()
        self._add_servicers()

    def _create_server(self):
        self._server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=settings.MAX_WORKERS),
            options=self._server_options(),
        )

    def _server_options(self):
        server_options = (
            # send keepalive every x milliseconds
            ("grpc.keepalive_time_ms", KEEPALIVE_TIME_MS),
            (
                "grpc.keepalive_timeout_ms",
                KEEPALIVE_TIMEOUT_MS,
            ),  # keepalive ping time out after x milliseconds
            (
                "grpc.keepalive_permit_without_calls",
                KEEPALIVE_PERMIT_WITHOUT_CALLS,
            ),  # allow keepalive pings when there's no gRPC calls
            (
                "grpc.http2.max_pings_without_data",
                MAX_PINGS_WITHOUT_DATA,
            ),  # allow unlimited amount of keepalive pings without data
            (
                "grpc.http2.min_time_between_pings_ms",
                MIN_TIME_BETWEEN_PINGS_MS,
            ),  # allow grpc pings from client every x milliseconds
            (
                "grpc.http2.min_ping_interval_without_data_ms",
                MIN_PING_INTERVAL_WITHOUT_DATA_MS,
            ),  # allow grpc pings from client without data every x milliseconds
        )
        return server_options

    #hook client request to serving routine
    def _add_servicers(self):
        add_LogServiceServicer_to_server(WriteLogServicer(), self._server)

    def setup_insecure_server(self):
        self._server.add_insecure_port(
            "[::]:{port}".format(port=settings.PORT)
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
