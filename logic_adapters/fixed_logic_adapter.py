from chatterbot.logic.logic_adapter import LogicAdapter
from chatterbot.comparisons import levenshtein_distance
from chatterbot.conversation import Statement
import re
import information.information as INFO
class FixedLogicAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(FixedLogicAdapter, self).__init__(**kwargs)
        pass
        # self.statements = [Statement("Bölüm mail adresimi öğrenebilirmiyim?"),
        #                    Statement("Bölüm mailim ne?"),
        #                    Statement("Mailimi söyleyebilirmisin"),
        #                    Statement("mailim ne?"),
        #                    Statement("Bölüm mailimi nasıl öğrenebilirim")]

    def process(self, input_statement):
        from chatterbot.conversation import Statement
        input_statement.question = self.chatbot.question
        confidence = 0
        response = ""
        if input_statement.question.withPlaceHolders == INFO.Q_STUDENT_NO:
            confidence = 1
            response = "Bölüm mailiniz: b" + input_statement.question.getInformation(INFO.Q_STUDENT_NO) + "@cs.hacettepe.edu.tr"
        return confidence, Statement(response)