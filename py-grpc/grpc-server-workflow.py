#!/bin/python

from concurrent import futures
import time
import json
import grpc

import workflow_pb2
import workflow_pb2_grpc

from workflow.engine import GenericWorkflowEngine
from functools import wraps

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
  

def print_data(obj, eng):
    """Print the data found in the token."""
    print obj

my_workflow_1 = [
    print_data
]

def run_workflow(message):
  jsonObj = json.loads(message)
  print "Workflow input header message %s" %(jsonObj['Header'])
  data = jsonObj['Body']   
  my_engine = GenericWorkflowEngine()
  my_engine.setWorkflow(my_workflow_1)
  my_engine.process(data)

class Workflow(workflow_pb2_grpc.WorkflowServicer):

  def SayHello(self, request, context):
    print "Recieve message: %s" % (request.name)
    return workflow_pb2.HelloReply(message='Hello, %s!' % request.name)

  def Running(self, request, context):
    print "Running ..."
    run_workflow(request.message)
    time.sleep(10)
    jsonObj = {
      "Header": "RunningResult",
      "Body": {
        "Code": 200,
        "Infor": "Finish workflow"
      }
    }
    return workflow_pb2.RunningResult(message=json.dumps(jsonObj))


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  workflow_pb2_grpc.add_WorkflowServicer_to_server(Workflow(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()