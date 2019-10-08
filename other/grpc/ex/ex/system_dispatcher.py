"""The Python implementation of the GRPC of Ironman"""

from concurrent import futures
import sys
import time
import logging

import grpc

import Ironman_pb2
import Ironman_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class SystemDispatcher(Ironman_pb2_grpc.SystemDispatcherServicer):

    def __init__(self):
        self.regist_table = {}

    def Regist(self, request, context):
        print("get regist Message, " + request.name + " " + request.address)
        self.regist_table[request.name] = request.address
        return Ironman_pb2.RegistResultMsg(status='ok')

    def GetAddress(self, request, context):
        print("get request Message, " + request.name)
        address_ret = self.regist_table.get(request.name, '')
        return Ironman_pb2.AddressReturnMsg(address=address_ret)


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Ironman_pb2_grpc.add_SystemDispatcherServicer_to_server(SystemDispatcher(), server)
    server_port = '[::]:' + port
    #server.add_insecure_port('[::]:50051')
    server.add_insecure_port(server_port)
    print('system dispatcher run port:' + server_port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve(sys.argv[1])
