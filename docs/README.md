# grpc_python
author: Pavel Lorenc

Evaluate app : gRPC to Mongo DB

## Getting Started

This project requires Docker to be installed.

### Quickstart

Running it then should be as simple as:

```console
$ make build
$ make run
```

### Testing

``make test``

### Stub generating
- In protos folder  edit gRPC interface ``grpc_logger.proto``  [Proto DSL definition](https://developers.google.com/protocol-buffers/docs/proto3)


- Generate stub files for Python 
``python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./grpc_logger.proto``
