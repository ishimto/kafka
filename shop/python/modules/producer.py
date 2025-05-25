import os
from kafka import KafkaProducer
import json



producer = KafkaProducer(bootstrap_servers=os.getenv("KAFKA"))

def produce_data(user_input):
    producer.send(topic='myshop', value=f"{user_input}".encode())
    producer.flush()
