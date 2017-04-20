
from containers.question import Question
from information.tracker import Tracker
import information.information as INFO
class Chatbot:
    def __init__(self):
        from chatterbot import ChatBot
        self.chatbot = ChatBot(
            "HÜBOT",
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            logic_adapters=[
                # {
                #     "import_path": "chatterbot.logic.BestMatch",
                #     "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                #     "response_selection_method": "chatterbot.response_selection.get_first_response"
                # }
                # "chatterbot.logic.MathematicalEvaluation",
                {"import_path": "logic_adapters.vector_logic_adapter.VectorLogicAdapter"},
                {"import_path": "logic_adapters.fixed_logic_adapter.FixedLogicAdapter"}

            ],
            database="chatbot",
            read_only=True  # don't train bot with user data
        )
        self.chatbot.tracker = Tracker()
        self.__train()

    def answer(self,text):
        print("")
        print("Question",text)
        self.chatbot.question = Question(text)
        self.chatbot.question.extractInformation()
        self.chatbot.question.show()
        print("\nAnswering..")
        rawResponse = self.chatbot.get_response(text).text
        response = self.__processResponse(rawResponse)
        self.chatbot.tracker.addConversation(text,rawResponse)
        return response

    def __train(self):
        return
        from chatterbot.trainers import ListTrainer
        from database.database import DataBase
        import conversation_helper

        conversations = conversation_helper.importConversations("./conversation_data/questions.txt")
        print("Training..", len(conversations))

        self.chatbot.set_trainer(ListTrainer)
        counter = 0
        for c in conversations:
            counter += 1
            print(counter)
            self.chatbot.train(c)
        print("Training is done!")

    def __processResponse(self,response):
        import re
        for p in re.findall("(<[^<>]*>)", response):
            if p == INFO.A_TIME:
                from datetime import datetime
                now = datetime.now()
                response = response.replace(p,'Saat ' + now.strftime('%H:%M'))
                pass
            else:
                response = response.replace(p,self.chatbot.question.getInformation(p))
        return response


