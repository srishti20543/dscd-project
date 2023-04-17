import sys
sys.path.insert(1, 'Protos')

from concurrent import futures
from multiprocessing import Process

import CommWithMaster_pb2_grpc
import CommWithMaster_pb2
import logging
import grpc
import Mapper
import Reducer
import os
from time import sleep


MAPPERS = 0
REDUCERS = 0
InputDir = ''
OutputDir = ''
RequestType = 0

class CommWithMasterServicer(CommWithMaster_pb2_grpc.CommWithMasterServicer):

    def MakeChoice(self, request, context):
        global RequestType, MAPPERS, REDUCERS, InputDir, OutputDir
        
        if request.typeOfRequest == 1 or request.typeOfRequest == 2 or request.typeOfRequest == 3:
            RequestType = request.typeOfRequest
            MAPPERS = request.mappers
            REDUCERS = request.reducers
            InputDir = request.in_dir
            OutputDir = request.out_dir
            forkMappers()
            sleep(1)
            forkReducers()
            return CommWithMaster_pb2.RegisterResponse(status="SUCCESS")
        else:
            return CommWithMaster_pb2.RegisterResponse(status="FAIL")


def forkMappers():
    if not os.path.exists('datafiles/intermediate'):
        os.makedirs('datafiles/intermediate')

    Mappers = []
    for i in range(MAPPERS):
            dir = ""
            if RequestType == 1:
                dir = InputDir + '/word_count/Input' + str(i+1) + '.txt'
            elif RequestType == 2:
                dir = InputDir + '/inverted_index/Input' + str(i+1) + '.txt'
            else:
                dir = InputDir + '/natural_join/Input' + str(i+1) + '.txt'
            Mappers.append(Process(target=Mapper.startMapper, args=(dir, RequestType, (i+1), REDUCERS)))
            Mappers[i].start()

def forkReducers():
    if not os.path.exists('datafiles/output'):
        os.makedirs('datafiles/output')
    
    Reducers = []
    for i in range(REDUCERS):
            dir = OutputDir + '/Output' + str(i+1) + '.txt'
            Reducers.append(Process(target=Reducer.startReducer, args=(dir, RequestType, (i+1), MAPPERS)))
            Reducers[i].start()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CommWithMaster_pb2_grpc.add_CommWithMasterServicer_to_server(CommWithMasterServicer(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()