import os
from kafka import KafkaConsumer
from pymongo import MongoClient
import json


KAFKA_BROKER = os.getenv("KAFKA")
TOPIC_NAME = 'myshop'

MONGO_URI = os.getenv("MONGO_LOGIN")
DB_NAME = 'shop'
COLLECTION_NAME = 'products'

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
products_collection = db[COLLECTION_NAME]

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    group_id='mongo_consumer'
    )

print(f"Listening to topic '{TOPIC_NAME}'...")

for message in consumer:
    product = message.value.decode('utf-8')
    print("Product input:", product)

    result = products_collection.delete_one({'name': product})
    
    if result.deleted_count > 0:
        print(f"Deleted product with name: {product}")
    else:
        print(f"Product '{product}' not found in MongoDB.")
