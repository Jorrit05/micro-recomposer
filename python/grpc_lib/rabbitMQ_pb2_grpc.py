# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import rabbitMQ_pb2 as rabbitMQ__pb2


class SideCarStub(object):
    """The sidecar definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitRabbitMq = channel.unary_unary(
                '/proto.SideCar/InitRabbitMq',
                request_serializer=rabbitMQ__pb2.ServiceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Consume = channel.unary_stream(
                '/proto.SideCar/Consume',
                request_serializer=rabbitMQ__pb2.ConsumeRequest.SerializeToString,
                response_deserializer=rabbitMQ__pb2.RabbitMQMessage.FromString,
                )
        self.SendRequestApproval = channel.unary_unary(
                '/proto.SideCar/SendRequestApproval',
                request_serializer=rabbitMQ__pb2.RequestApproval.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendValidationResponse = channel.unary_unary(
                '/proto.SideCar/SendValidationResponse',
                request_serializer=rabbitMQ__pb2.ValidationResponse.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendCompositionRequest = channel.unary_unary(
                '/proto.SideCar/SendCompositionRequest',
                request_serializer=rabbitMQ__pb2.CompositionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendSqlDataRequest = channel.unary_unary(
                '/proto.SideCar/SendSqlDataRequest',
                request_serializer=rabbitMQ__pb2.SqlDataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class SideCarServicer(object):
    """The sidecar definition.
    """

    def InitRabbitMq(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Consume(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRequestApproval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendValidationResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCompositionRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSqlDataRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SideCarServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitRabbitMq': grpc.unary_unary_rpc_method_handler(
                    servicer.InitRabbitMq,
                    request_deserializer=rabbitMQ__pb2.ServiceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Consume': grpc.unary_stream_rpc_method_handler(
                    servicer.Consume,
                    request_deserializer=rabbitMQ__pb2.ConsumeRequest.FromString,
                    response_serializer=rabbitMQ__pb2.RabbitMQMessage.SerializeToString,
            ),
            'SendRequestApproval': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRequestApproval,
                    request_deserializer=rabbitMQ__pb2.RequestApproval.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendValidationResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.SendValidationResponse,
                    request_deserializer=rabbitMQ__pb2.ValidationResponse.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendCompositionRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCompositionRequest,
                    request_deserializer=rabbitMQ__pb2.CompositionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendSqlDataRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSqlDataRequest,
                    request_deserializer=rabbitMQ__pb2.SqlDataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.SideCar', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SideCar(object):
    """The sidecar definition.
    """

    @staticmethod
    def InitRabbitMq(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.SideCar/InitRabbitMq',
            rabbitMQ__pb2.ServiceRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Consume(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.SideCar/Consume',
            rabbitMQ__pb2.ConsumeRequest.SerializeToString,
            rabbitMQ__pb2.RabbitMQMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRequestApproval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.SideCar/SendRequestApproval',
            rabbitMQ__pb2.RequestApproval.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendValidationResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.SideCar/SendValidationResponse',
            rabbitMQ__pb2.ValidationResponse.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendCompositionRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.SideCar/SendCompositionRequest',
            rabbitMQ__pb2.CompositionRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSqlDataRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.SideCar/SendSqlDataRequest',
            rabbitMQ__pb2.SqlDataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)