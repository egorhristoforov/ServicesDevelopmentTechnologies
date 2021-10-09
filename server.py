from concurrent import futures
import logging

import grpc
from ProtocolsOut import greeting_service_pb2
from ProtocolsOut import greeting_service_pb2_grpc

PORT="50051"

class Greeting(greeting_service_pb2_grpc.GreetingServicer):

    def GetHello(self, request, context):
        return greeting_service_pb2.HelloResponse(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_service_pb2_grpc.add_GreetingServicer_to_server(Greeting(), server)
    server.add_insecure_port("[::]:{0}".format(PORT))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
    logging.info('Server started on port {0}'.format(PORT))