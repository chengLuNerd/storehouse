from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "amqp://guest:guest@127.0.0.1:5672//"  # e.g. "pyamqp://guest:guest@localhost"
}


with ClusterRpcProxy(config) as cluster_rpc:
    
    result = cluster_rpc.service_x.remote_method("hellø")
    print(result)
    

    """
    hello_res = cluster_rpc.service_x.remote_method.call_async("hello")
    world_res = cluster_rpc.service_x.remote_method.call_async("world")


    print(hello_res.result())  # "hello-x-y"
    print(world_res.result())  # "world-x-y"


    cluster_rpc.service_dispatch.dispatching_method.call_async('100')
    """
