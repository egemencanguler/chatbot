from chatterbot.logic.logic_adapter import LogicAdapter
import re
class FixedLogicAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(FixedLogicAdapter, self).__init__(**kwargs)


    def process(self, input_statement):
        from chatterbot.conversation import Statement
        confidence = 0
        response = ""
        text = input_statement.text.lower().strip()
        match = re.match(r'(\d{8})',text)
        print(text,match)
        if match:
            confidence = 1
            response = "Bölüm mailiniz: b" + match.group(1) + "@cs.hacettepe.edu.tr"
        return confidence, Statement(response)