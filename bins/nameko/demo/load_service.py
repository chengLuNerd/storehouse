from nameko.events import BROADCAST, event_handler, SERVICE_POOL, EventDispatcher
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy
import time
import requests
import json

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}

class ServiceLoad:
    """ Event listening service. """
    name = "service_load"

    dispatch = EventDispatcher()

    @event_handler("service_dispatch", "load", handler_type=SERVICE_POOL)
    def handle_event(self, studyUID):
        print("service load received:", studyUID)


        time.sleep(10)
        print("end to download dicom file ", studyUID)
        
        print("request to compute queue  ", studyUID)
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.service_dispatch.dispatching_compute.call_async(studyUID)
























        """
        GET_HIERACHY_URL = 'http://10.3.14.149:8081/get/Home/ImageService?CommandType=GetHierachy&StudyUID=1.3.6.1.4.1.9328.50.6.90317'
        GET_IMAGE_URL = 'http://10.3.14.149:8081/get/Home/ImageService?CommandType=GetImage&ContentType=application/dicom&ObjectUID='

        print("begin to download dicom file to fileserver")

        r= requests.get(GET_HIERACHY_URL)
        
        content = r.json()

        studyList = content['PatientInfo']['StudyList']

        for studyInfo in studyList:
            studyUID = studyInfo['UID']
            print("study id is ", studyUID)

            seriesList = studyInfo['SeriesList']
            for series in seriesList:
            seriesUID = series['UID']
            print("series id is ", seriesUID, "\n")
            time.sleep(3)

            imageList = series['ImageList']
            print(len(imageList))
                for image in imageList:
                    sopUID = image['UID']
                    imageURL = GET_IMAGE_URL+sopUID
                    print("image id is ", sopUID)
                    imageContent = requests.get(imageURL)
                    with open(sopUID+'.dcm',  'wb') as imageFile:
                        for chunk in imageContent.iter_content(100000):
                            imageFile.write(chunk)
        """


    
