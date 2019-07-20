"""The Python implementation of the GRPC of Ironman"""

from concurrent import futures
import sys
import time
import logging

import grpc

import Ironman_pb2
import Ironman_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class BackendRender(Ironman_pb2_grpc.BackendRenderServicer):

    def InitHandler(self, request, context):
        print("get init Message, " + request.name)
        return Ironman_pb2.InitReply(message='init, %s!' % request.name)

    def RenderHandler(self, request, context):
        return Ironman_pb2.RenderReply(message='render, %s!' % request.name)

def registe_dispatcher(srvname, addr):
    with grpc.insecure_channel('localhost:10000') as channel:
        stub = Ironman_pb2_grpc.SystemDispatcherStub(channel)
        response = stub.Regist(Ironman_pb2.RegistMsg(name=srvname, address=addr))
        print("get dispatcher status " + response.status)

def serve(port, srvname):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Ironman_pb2_grpc.add_BackendRenderServicer_to_server(BackendRender(), server)
    server_port = '[::]:' + port
    #server.add_insecure_port('[::]:50051')
    server.add_insecure_port(server_port)
    print('server run port:' + server_port)
    server.start()

    registe_dispatcher(srvname, 'localhost:'+port)

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve(sys.argv[1], sys.argv[2])
