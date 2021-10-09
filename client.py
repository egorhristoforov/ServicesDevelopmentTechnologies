import logging
import grpc
from ProtocolsOut import greeting_service_pb2
from ProtocolsOut import greeting_service_pb2_grpc

PORT="50051"

def run():
    with grpc.insecure_channel('localhost:{0}'.format(PORT)) as channel:
        stub = greeting_service_pb2_grpc.GreetingStub(channel)

        while True:
            name = input("Enter your name: ")
            response = stub.GetHello(greeting_service_pb2.HelloRequest(name=name))
            print("Greeting service response:\n{0}".format(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()