from pymongo import MongoClient


MONGO_URI = 'mongodb://root:changeme@mongodb.default.svc.cluster.local:27017'
DB_NAME = 'shop'
COLLECTION_NAME = 'products'

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
products_collection = db[COLLECTION_NAME]


def products_list():
    pipeline = [
        {"$group": {"_id": "$name", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    results = products_collection.aggregate(pipeline)
    return "\n".join(f"{doc['_id']}:{doc['count']}" for doc in results)

