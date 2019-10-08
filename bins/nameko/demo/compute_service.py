from nameko.events import BROADCAST, event_handler, SERVICE_POOL
from nameko.rpc import rpc
import time
import requests
import json

class ServiceCompute:
    """ Event listening service. """
    name = "service_compute"

    @event_handler("service_dispatch", "compute", handler_type=SERVICE_POOL)
    def handle_event(self, studyUID):
        print("service compute received: ", studyUID)
        for i in range(10):
            print("busy to compute, please wait", studyUID)
            time.sleep(2)
        print("service compute end :", studyUID)
       


    
