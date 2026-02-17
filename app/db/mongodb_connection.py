from pymongo import MongoClient

from core.config import settings
class MongoDB():
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod    
    def _get_connection():
        if MongoDB._connection is None:
            MongoDB._connection = MongoClient(settings.DATABASE_URL)
            print('Connected to MongoDB...')
        return MongoDB._connection

    @staticmethod
    def _db(client):
        db = client[settings.MONGO_INITDB_DATABASE]
        return db 
    
    @staticmethod
    def get_collection(collection_name):
        conn = MongoDB._get_connection()
        db = MongoDB._db(conn)
        coll = db[collection_name]
        return coll






