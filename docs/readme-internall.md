### Stub generating
 python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_logger.proto

 python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./system_info.proto

  python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./grpc_logger.proto

### Technologies
- Marshmallow
- gRPC
- MongoDB
- [ODM engines for Python](https://project-awesome.org/mjhea0/awesome-fastapi#databases)
- Pydantic settings

### Mongo configuration
- localhost:27017