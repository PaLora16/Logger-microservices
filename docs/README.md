# Logger  microservice

author: Pavel Lorenc


This microservice accepts gRPC calls from different clients, storing log records into Mongo DB.

An example of how to employ [gRPC](https://grpc.io/docs/languages/python/basics/) in the real world.
There is **grpc_logger_services** and **client** part. Client prepares Log object, then write one to Log services
The Log data model supports standard log level, log message, and log agenda. Log agenda enables distinguishing between different clients, thus enabling logging in one Mongo DB multiple apps.
This demo just writes a log as the following functionality is open to extension.
The main reason was to show functional gRPC plumbing.

## Used technologies

- MongoDB
- gRPC
- Pydantic confi
- ODM beanie

### Instalation

- Install MongoDB locally
- clone project locally
- create venv and run ``pip install -r requirements.txt`` from cloned folder

- run server instance ``python serve.py``
- run client instance ``python log_write.py``

### Stub generating

- In protos folder  edit gRPC interface ``grpc_logger.proto``  [Proto DSL definition](https://developers.google.com/protocol-buffers/docs/proto3)

- Generate stub files for Python
``python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./grpc_logger.proto``
