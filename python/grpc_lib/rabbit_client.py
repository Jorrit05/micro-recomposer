import grpc
import os
import time

import rabbitMQ_pb2_grpc as rabbit
import rabbitMQ_pb2 as rabbitTypes
from grpc_lib import SecureChannel


class RabbitClient(SecureChannel):
    def __init__(self, grpc_addr, service_name, routing_key, auto_delete_queue, callback=None):
        super().__init__(grpc_addr, os.getenv("SIDECAR_PORT"))
        self.client = rabbit.SideCarStub(self.channel)
        service_request = rabbitTypes.ServiceRequest()
        service_request.service_name = service_name
        service_request.routing_key = routing_key
        service_request.queue_auto_delete = auto_delete_queue
        self.callback = callback
        self.stop_consuming = False
        self.initialize_rabbit(service_request)

    def initialize_rabbit(self, service_request):
        try:
            self.client.InitRabbitMq(service_request)
            self.logger.debug("Rabbit service started successfully")
        except grpc.RpcError as e:
            self.logger.warning(f"Attempt : could not establish connection with RabbitMQ: {e}")

    def close_program(self):
        # Call this function to close gRPC channel gracefully
        self.channel.close()
        self.logger.debug("Closed gRPC connection")

    def start_consuming(self, queue_name, max_retries=5, wait_time=1):
        self._consume_with_retry(queue_name, max_retries, wait_time)

    def _consume_with_retry(self, queue_name, max_retries, wait_time):
        for i in range(max_retries):
            try:
                self._consume(queue_name)
                return
            except grpc.RpcError as e:
                self.logger.error(f"Failed to start consuming (attempt {i+1}/{max_retries}): {e}")
                if self.stop_consuming:  # Check if we've been told to stop before handling each response
                    return
                time.sleep(wait_time)

    def _consume(self, queue_name):
        consume_request = rabbitTypes.ConsumeRequest()
        consume_request.queue_name = queue_name
        consume_request.auto_ack = True

        try:
            responses = self.client.Consume(consume_request)
            for response in responses:
                self._handle_response(response)
                if self.stop_consuming:  # Check if we've been told to stop before handling each response
                    return
        except grpc.RpcError as e:
            self.logger.error(f"Error on consume: {e}")
            raise e

    def _handle_response(self, response):
        # Call the callback function, if it exists, and pass the RabbitClient instance (self)
        if self.callback:
            self.stop_consuming = self.callback(self, response)
