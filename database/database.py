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
        self.tr_vectors = self.client.hubot.tr_vectors
        self.tr_sentence = self.client.hubot.tr_sentence
        pass

    def insertVector(self,word,vector):
        data = {"_id":word, "vec":vector}
        self.tr_vectors.insert_one(data)

    def getVector(self,word):
        data = self.tr_vectors.find_one({"_id":word})
        if data is None:
            return None
        return data["vec"]

    def cacheSentence(self,sentence,vector):
        data = {"_id": sentence, "vec": vector}
        self.tr_sentence.insert_one(data)

    def getSentenceVector(self,sentence):
        data = self.tr_sentence.find_one({"_id": sentence})
        if data is None:
            return None
        return data["vec"]

