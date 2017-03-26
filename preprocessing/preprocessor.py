import re
import information as Info


# regular expression and corresponding placeholder tokens
regexs = [
    [r'(\d{8})',Info.STOKEN_STUDENT_NO]
    ,[r'([a-z]{3}) ?(\d{3})',Info.STOKEN_COURSE_CODE]
    ,[r'(d) ?(\d\d?)',Info.STOKEN_CLASSROOM]
    ,[r'(d)erslik ?(\d\d?)',Info.STOKEN_CLASSROOM]
]


class Preprocessor:

    def __init__(self):
        from preprocessing.stemmer import Stemmer
        self.stemmer = Stemmer()
        pass

    def process(self,question):
        text = question.raw.lower()
        # Extract information from text and replace common structures
        for r in regexs:
            match = re.search(r[0],text)
            if match:
                value = None
                if r[1] == Info.STOKEN_COURSE_CODE or r[1] == Info.STOKEN_CLASSROOM:
                    value = match.group(1) + match.group(2)
                else:
                    value = match.group(1)
                question.putInformation(r[1],value)
                text = re.sub(r[0],r[1],text)
        question.processed = text
        question.stemmed = self.stemmer.stem(question.raw)
        print(text)
        return question