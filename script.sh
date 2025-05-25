#!/bin/bash


helm install kafka kafka/helm/
helm install mongodb mongodb/helm/
helm install app shop/helm/
