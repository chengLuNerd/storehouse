from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc


class ServiceDispatch:
    """ Event dispatching service. """
    name = "service_dispatch"

    dispatch = EventDispatcher()

    @rpc
    def dispatching_load(self, studyUID):
        self.dispatch("load", studyUID)


    @rpc
    def dispatching_compute(self, studyUID):
        self.dispatch("compute", studyUID)

