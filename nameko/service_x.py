from nameko.rpc import rpc, RpcProxy

class ServiceX:
    name="service_x"

    y = RpcProxy('service_y')

    @rpc
    def remote_method(self, value):
        res = u"{}-x".format(value)
        return self.y.append_identifier(res)
