import os
import pymongo
import pymongo.collation
from bson import ObjectId
import time

class MongoDatabase(object):
        def __init__(self): 
                self.client = pymongo.MongoClient(os.environ.get("MONGO_DATABASE_HOST"), tls=True, tlsCAFile='app/functions/certs/us-west-2-bundle.pem')
                self.DATABASE = self.client[os.environ.get("MONGO_DATABASE_NAME")]
                
        def find(self, collection, query):
            return self.DATABASE[collection].find(query)

        def find_one(self, collection, query):
            return self.DATABASE[collection].find_one(query)

        def aggregate(self, collection, query):
            return self.DATABASE[collection].aggregate(query)

        def find_one_and_update(self, collection, id, fieldArray, username, companyid): 
            return self.DATABASE[collection].find_one_and_update(
                {'_id' : ObjectId(id) }, {"$set": fieldArray })
            
        def insert(self, collection,fieldArray): 
            x = self.DATABASE[collection].insert_one(fieldArray)
            return x

class BaseDBObject(object):     
        def __init__(self):    
                self.created = round(time.time() * 1000)
                self.modified = round(time.time() * 1000)
                self.deleted = False
                self.updated = False
       
        
class sql_error_log(BaseDBObject):
        def __init__(self, sql):
                self.sql = sql
                BaseDBObject.__init__(self)
