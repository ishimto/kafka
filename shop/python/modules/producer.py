from kafka import KafkaProducer
import json



producer = KafkaProducer(bootstrap_servers='kafka-broker-0.kafka-headless.default.svc.cluster.local:9092')

def produce_data(user_input):
    producer.send(topic='myshop', value=f"{user_input}".encode())
    producer.flush()
