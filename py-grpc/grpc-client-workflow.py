#!/bin/python

from __future__ import print_function

import grpc

import workflow_pb2
import workflow_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = workflow_pb2_grpc.WorkflowStub(channel)

  response = stub.Running(workflow_pb2.RunningRequest(message='Running request'))
  print("Running client received: " + response.message)


if __name__ == '__main__':
  run()
