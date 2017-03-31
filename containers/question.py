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
        self.__extractInformation()



    def putInformation(self,key,info):
        self.information[key] = info

    def getInformation(self,key):
        if key in self.information:
            return self.information[key]
        else:
            return None

    def __replacePlaceHolders(self,text):
        # Extract information from text and replace common structures
        for r in regexs:
            match = re.search(r[0],text)
            if match:
                value = None
                if r[1] == INFO.Q_COURSE_CODE or r[1] == INFO.Q_CLASSROOM:
                    value = match.group(1) + match.group(2)
                else:
                    value = match.group(1)
                self.putInformation(r[1],value)
                text = re.sub(r[0],r[1],text)
        return text

    def __tokenize(self,text):
        punctuations = (r"\.", r":", r";", r"\?", ",", "!")
        tokens = []
        text = text.strip()
        # processed = re.sub(r'<.*>', '', text)
        for p in punctuations:
            text = re.sub(p, " " + p.replace("\\", ""), text)
        tokens += [t for t in re.split(" +", text) if t != ""]
        return tokens

    def show(self):
        print("Raw:",self.raw)
        print("Clean:",self.clean)
        print("CleanTokenized:",self.cleanTokenized)
        print("WithplaceHolders:",self.withPlaceHolders)
        print("WithplaceHoldersTokenized",self.withPlaceHoldersTokenized)
        print("Information:",self.information)

    def getName(self):
        from difflib import SequenceMatcher
        import chatterbot.comparisons
        similarity = 0
        name = None
        for n in INFO.PEOPLE.keys():
            sim = SequenceMatcher(
                None,
                n,
                self.clean
            )
            percent = round(sim.ratio(), 2)
            if percent > similarity:
                name = n
                similarity = percent
        return name

    def __extractInformation(self):
        name = self.getName()
        self.information[INFO.Q_NAME] = self.getName()
        self.information[INFO.A_OFFICE] = INFO.PEOPLE[name]["office"]
        self.information[INFO.A_MAIL] = INFO.PEOPLE[name]["mail"]
        self.information[INFO.A_TEL] = INFO.PEOPLE[name]["tel"]
        self.information[INFO.A_RESEARCH_AREAS] = INFO.PEOPLE[name]["research"]
        self.information[INFO.A_WEBSITE] = INFO.PEOPLE[name]["website"]
        if INFO.Q_CLASSROOM in self.information:
            self.information[INFO.A_CLASSROOM_LOC] = INFO.LOCATIONS[self.information[INFO.Q_CLASSROOM]]
