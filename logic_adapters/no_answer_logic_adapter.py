from chatterbot.logic.logic_adapter import LogicAdapter
import re

answers = ["Kusura bakmayın bu sorunun cevabını bilmiyorum.",
           "Lütfen soruyu başka bir şekilde ifade etmeyi deneyin."]

threshold = 0.5

class NoAnswerAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(NoAnswerAdapter, self).__init__(**kwargs)


    def process(self, input_statement):
        from chatterbot.conversation import Statement
        import random
        confidence = threshold
        response = answers[random.randint(0,len(answers)-1)]
        return confidence, Statement(response)