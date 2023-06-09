package main

import (
	pb "github.com/Jorrit05/DYNAMOS/pkg/proto"
	amqp "github.com/rabbitmq/amqp091-go"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/anypb"
)

// Handle incoming AMQ messages.
// Stream functionality to send responses to the 'main' container. Create a RabbitMQMessage type by making sure the type is easily accessible
// and package the body.
func (s *server) handleResponse(msg amqp.Delivery, stream pb.SideCar_ConsumeServer, pbMsg proto.Message) error {
	proto.Reset(pbMsg)

	if err := proto.Unmarshal(msg.Body, pbMsg); err != nil {
		logger.Sugar().Errorf("Error unmarshalling proto msg, %v", err)
		return err
	}

	any, err := anypb.New(pbMsg)
	if err != nil {
		logger.Sugar().Error(err)
		return err
	}

	grpcMsg := &pb.RabbitMQMessage{
		Body: any,
		Type: msg.Type,
	}

	return stream.SendMsg(grpcMsg)
}

func (s *server) handleValidationResponse(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
	return s.handleResponse(msg, stream, &pb.ValidationResponse{})
}

func (s *server) handleRequestApprovalResponse(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
	return s.handleResponse(msg, stream, &pb.RequestApproval{})
}

func (s *server) handleCompositionRequestResponse(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
	return s.handleResponse(msg, stream, &pb.CompositionRequest{})
}

func (s *server) handleSqlDataRequest(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
	logger.Debug("Starting handleSqlDataRequest")
	return s.handleResponse(msg, stream, &pb.SqlDataRequest{})
}

func (s *server) handleMicroserviceCommunication(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
	logger.Debug("Starting handleMicroserviceCommunication")
	return s.handleResponse(msg, stream, &pb.MicroserviceCommunication{})
}

// func (s *server) handleSqlDataRequestResponse(msg amqp.Delivery, stream pb.SideCar_ConsumeServer) error {
// 	logger.Debug("Starting handleSqlDataRequestResponse")
// 	return s.handleResponse(msg, stream, &pb.SqlDataRequestResponse{})
// }
