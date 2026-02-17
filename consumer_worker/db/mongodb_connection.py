from pymongo import mongo_client
import pymongo
from core.config import settings

def _connection():
    client = mongo_client.MongoClient(settings.DATABASE_URL)
    print('Connected to MongoDB...')
    return client

def _db(client):
    db = client[settings.MONGO_INITDB_DATABASE]
    return db 
def get_collection(collection_name):
    conn = _connection()
    db = _db(conn)
    coll = db[collection_name]
    return coll


