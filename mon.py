import pymongo
from pymongo import MongoClient


class dbase:

    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://shreyakarmakar:shreyakarmakar@cluster0.2nz3sbm.mongodb.net/?retryWrites=true&w=majority")

        self.db = client.test
        print(self.db)
        pass

    def get_collection(self, name):
        menu = self.db.menu
        return menu
        pass

    def add_to_collection(self, collection, item):
        collection.insert_one(item.__dict__)
        pass
