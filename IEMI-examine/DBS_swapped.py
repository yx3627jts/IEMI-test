from pymongo import MongoClient #导入pymongo

class DBS_swapped:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.collection = self.client['pythonDBS']['usersData']

    def insertOneData(self,data):
        ret = self.collection.insert_one(data)
        return ret

    def insertManyData(self,data):
        ret = self.collection.insert_many(data)
        return ret

    def findOneData(self):
        ret = self.collection.find_one()
        return ret

    def findAllData(self):
        ret = self.collection.find()
        return ret

    def updateOneData(self,position,data):
        ret = self.collection.update_one(position, data)
        return ret