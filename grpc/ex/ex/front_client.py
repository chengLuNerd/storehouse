
"""The Python implementation of the GRPC Ironman client."""

from __future__ import print_function
import sys
import logging

import grpc

import Ironman_pb2
import Ironman_pb2_grpc


def get_app_addr(app_name):
    with grpc.insecure_channel('localhost:10000') as channel:
        stub = Ironman_pb2_grpc.SystemDispatcherStub(channel)
        response = stub.GetAddress(Ironman_pb2.AddressMsg(name=app_name))
        print("get dispatcher return addr: " + response.address)
        return response.address


def run(app_name):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    remote_port = get_app_addr(app_name)
    print("Try to connect remote: " + remote_port)
    with grpc.insecure_channel(remote_port) as channel:
        stub = Ironman_pb2_grpc.BackendRenderStub(channel)
        response = stub.InitHandler(Ironman_pb2.InitCommand(name='lucheng'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run(sys.argv[1])
