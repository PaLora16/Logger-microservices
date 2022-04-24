## Example how to generate stub

  python -m grpc_tools.protoc -I. --python_out=./proto_lib --grpc_python_out=./proto_lib ./grpc_logger.proto

### Usage
Generated stubs copy to server folder beside server.py  
  