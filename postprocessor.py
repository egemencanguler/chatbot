import re
import information as Info


class Postprocessor:

    def __init__(self):
        self.im = Info.InformationManager()

    def process(self,text):
        # Replace placeholder statement tokens with real values
        for i in Info.STATEMENT_TOKENS:
            value = self.im.getTokenValue(i)
            if value != None:
                text = text.replace(i,value)

        # Replace asnwer tokens with corresponding information
        for i in Info.ANSWER_TOKENS:
            if text.find(i) != -1:
                info = self.im.getInfo(i)
                text = text.replace(i,info)

        return text

    def replace(self,text,key,value):
        m = re.match(key,text)