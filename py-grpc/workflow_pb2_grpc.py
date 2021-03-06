# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import workflow_pb2 as workflow__pb2


class WorkflowStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/workflow.Workflow/SayHello',
        request_serializer=workflow__pb2.HelloRequest.SerializeToString,
        response_deserializer=workflow__pb2.HelloReply.FromString,
        )
    self.Running = channel.unary_unary(
        '/workflow.Workflow/Running',
        request_serializer=workflow__pb2.RunningRequest.SerializeToString,
        response_deserializer=workflow__pb2.RunningResult.FromString,
        )


class WorkflowServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Running(self, request, context):
    """Sends another greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkflowServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=workflow__pb2.HelloRequest.FromString,
          response_serializer=workflow__pb2.HelloReply.SerializeToString,
      ),
      'Running': grpc.unary_unary_rpc_method_handler(
          servicer.Running,
          request_deserializer=workflow__pb2.RunningRequest.FromString,
          response_serializer=workflow__pb2.RunningResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'workflow.Workflow', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
