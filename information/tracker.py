class Tracker:
    def __init__(self):
        self.stack = []


    def addConversation(self,question,answer):
        self.stack.append([question,answer])

    def getLastAnswer(self):
        return self.stack[-1][1]

    def getLastQuestion(self):
        return self.stack[-1][0]