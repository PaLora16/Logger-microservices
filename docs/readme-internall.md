## Stub generating
 python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_logger.proto

 python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./system_info.proto

  python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./grpc_logger.proto

## Technologies
- Marshmallow
- gRPC
- MongoDB
- Prisma Client Python  