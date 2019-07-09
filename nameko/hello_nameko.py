from nameko.rpc import rpc, RpcProxy

class GreetingService:
    name = "greeting_service"

    @rpc  # `method` is exposed over RPC
    def hello(self):
        # application logic goes here
        return "hello, boy"
