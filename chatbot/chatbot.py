
import information.information as INFO
class Chatbot:
    def __init__(self):
        from chatterbot import ChatBot
        self.chatbot = ChatBot(
            "HÜBOT",
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            logic_adapters=[
                {"import_path": "logic_adapters.vector_logic_adapter.VectorLogicAdapter"},
                {"import_path": "logic_adapters.fixed_logic_adapter.FixedLogicAdapter"},
                {"import_path": "logic_adapters.no_answer_logic_adapter.NoAnswerAdapter"}

            ],
            database="chatbot",
            read_only=True  # don't train bot with user data
        )

    def answer(self,text):
        print("Question",text)
        print("\nAnswering..")
        rawResponse = self.chatbot.get_response(text).text
        response = self.__processResponse(rawResponse)
        return response

    def train(self,path):
        from chatterbot.trainers import ListTrainer
        import conversation_helper
        conversations = conversation_helper.importConversations(path)
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
        return response


