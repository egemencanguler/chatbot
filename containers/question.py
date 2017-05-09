import re
import information.information as INFO
import nltk

# regular expression and corresponding placeholder tokens
regexs = [
    [r'(\d{8})',INFO.Q_STUDENT_NO]
    ,[r'([a-z]{3}) ?(\d{3})',INFO.Q_COURSE_CODE]
    ,[r'(d) ?(\d\d?)',INFO.Q_CLASSROOM]
    ,[r'(d)erslik ?(\d\d?)',INFO.Q_CLASSROOM]
]

class Question:
    def __init__(self,raw):
        self.information = {}
        self.raw = raw
        self.clean = raw.lower().strip()
        self.cleanTokenized = self.__tokenize(self.clean)
        self.withPlaceHolders = self.__replacePlaceHolders(self.clean)
        self.withPlaceHoldersTokenized = self.__tokenize(self.withPlaceHolders)


    def putInformation(self,key,info):
        self.information[key] = info

    def getInformation(self,key):
        if key in self.information:
            return self.information[key]
        else:
            return None

    def __tokenize(self,text):
        punctuations = (r"\.", r":", r";", r"\?", ",", "!")
        tokens = []
        text = text.strip()
        # processed = re.sub(r'<.*>', '', text)
        for p in punctuations:
            text = re.sub(p, " " + p.replace("\\", ""), text)
        tokens += [t for t in re.split(" +", text) if t != ""]
        return tokens
