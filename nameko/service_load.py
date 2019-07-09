from nameko.events import BROADCAST, event_handler, SERVICE_POOL 
from nameko.rpc import rpc
import time

class ServiceLoad:
    """ Event listening service. """
    name = "service_load"

    @event_handler("service_dispatch", "load", handler_type=SERVICE_POOL)
    def handle_event(self, payload):
        print("service load received:", payload)
        time.sleep(7)
