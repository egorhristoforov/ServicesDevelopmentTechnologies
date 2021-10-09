INPUTFOLDER="./Protocols"
OUTPUTFOLDER=$INPUTFOLDER"Out"
INPUTFILE="greeting_service.proto"

mkdir -p $OUTPUTFOLDER

python -m grpc_tools.protoc -I$INPUTFOLDER --python_out=$OUTPUTFOLDER --grpc_python_out=$OUTPUTFOLDER $INPUTFOLDER/$INPUTFILE

# NOTE: Workaround for https://github.com/protocolbuffers/protobuf/issues/4546
sed -i '' 's/^\(import.*pb2\)/from . \1/g' $OUTPUTFOLDER/*.py