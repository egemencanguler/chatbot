from chatterbot.logic.logic_adapter import LogicAdapter
from chatterbot.comparisons import levenshtein_distance
from chatterbot.conversation import Statement
import re
import information as Info
class EmailLogicAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(EmailLogicAdapter, self).__init__(**kwargs)
        self.questionAsked = False
        self.statements = [Statement("Bölüm mail adresimi öğrenebilirmiyim?"),
                           Statement("Bölüm mailim ne?"),
                           Statement("Mailimi söyleyebilirmisin"),
                           Statement("mailim ne?"),
                           Statement("Bölüm mailimi nasıl öğrenebilirim")]

    def process(self, statement):
        from chatterbot.conversation import Statement
        text = statement.text.lower()
        if self.questionAsked:
            self.questionAsked = False
            match = re.match(Info.TOKEN_STUDENT_NO,text)
            if match:
                return 1, Statement("Bölüm mailiniz: b" + Info + "@cs.hacettepe.edu.tr")
        confidence = 0
        response = "Öğrenci numaranızı yazarsanız yardımcı olabilirim."
        for s in self.statements:
            confidence = levenshtein_distance(s, statement)
            if confidence > 0.5:
                self.questionAsked = True
                break
        return confidence, Statement(response)