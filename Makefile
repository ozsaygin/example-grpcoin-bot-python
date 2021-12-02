generate-protos:
	poetry run \
		python -m grpc_tools.protoc \
		-I ./protos \
		--python_out=./grpcoin/generated/ \
		--grpc_python_out=./grpcoin/generated/ \
		./protos/grpcoin.proto