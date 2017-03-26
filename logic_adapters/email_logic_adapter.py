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
        self.im = Info.InformationManager()

    def process(self, statement):
        from chatterbot.conversation import Statement
        text = statement.text.lower()
        if self.questionAsked:
            print("HEY", statement, ", ", Info.STOKEN_STUDENT_NO)
            self.questionAsked = False
            match = re.match(Info.STOKEN_STUDENT_NO,text)
            if statement == Info.STOKEN_CLASSROOM:
                print(" LOLO")
                return 1, Statement("Bölüm mailiniz: b" + Info.STOKEN_STUDENT_NO + "@cs.hacettepe.edu.tr")
        confidence = 0
        response = "Öğrenci numaranızı yazarsanız yardımcı olabilirim."
        for s in self.statements:
            confidence = levenshtein_distance(s, statement)
            if confidence > 0.5:
                print("hooo")
                self.questionAsked = True
                break
        return confidence, Statement(response)