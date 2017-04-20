class DataBase:
    # Singleton
    __instance = None

    def __new__(cls):
        if DataBase.__instance is None:
            DataBase.__instance = object.__new__(cls)
            DataBase.__instance.statementTokens = {}
        return DataBase.__instance

    def __init__(self):
        from pymongo import MongoClient
        self.client = MongoClient()
        self.tr_vectors = self.client.tr_vectors.tr_vectors
        self.tr_sentence = self.client.tr_sentence
        pass

    def insertVector(self,word,vector):
        data = {"_id":word, "vec":vector}
        self.tr_vectors.insert_one(data)

    def getVector(self,word):
        data = self.tr_vectors.find_one({"_id":word})
        if data == None:
            return None
        return data["vec"]




# file = open("/Users/macbook/Desktop/vectors_gencor.tur.txt","r")
# from database.database import DataBase
# db = DataBase()
# # print(db.getVector("</s>"))
# #
# counter = 0
# lines = []
# for line in file:
#     tokens = line.split(" ")
#     word = tokens[0]
#     vector = []
#     for i in range(1,201):
#         data = tokens[i].strip()
#         vector.append(float(data))
#     db.insertVector(word,vector)
# file.close()