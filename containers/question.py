class Question:
    def __init__(self,raw):
        self.raw = raw
        self.processed = ""
        self.stemmed = ""
        self.information = {}

    def putInformation(self,key,info):
        self.information[key] = info

    def getInformation(self,key):
        if key in self.information:
            return self.information[key]
        else:
            return None

    def __str__(self):
        return "Raw: " + self.raw + "\n" \
                "Processed: " + self.processed + "\n" \
                "Stemmed: " + self.stemmed + "\n"