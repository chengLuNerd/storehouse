from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc


class ServiceDispatch:
    """ Event dispatching service. """
    name = "service_dispatch"

    dispatch = EventDispatcher()

    @rpc
    def dispatching_method(self, payload):
        self.dispatch("load", payload)

