//go:build !local
// +build !local

package main

var serviceName = "policyEnforcer"

var etcdEndpoints = "http://etcd-0.etcd-headless.core.svc.cluster.local:2379,http://etcd-1.etcd-headless.core.svc.cluster.local:2379,http://etcd-2.etcd-headless.core.svc.cluster.local:2379"

var grpcAddr = "localhost:3005"