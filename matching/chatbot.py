
from containers.question import Question
class Chatbot:
    def __init__(self):
        from chatterbot import ChatBot
        self.chatbot = ChatBot(
            "HÜBOT",
            storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
            logic_adapters=[
                # {
                #     "import_path": "chatterbot.logic.BestMatch",
                #     "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                #     "response_selection_method": "chatterbot.response_selection.get_first_response"
                # }
                # "chatterbot.logic.MathematicalEvaluation",
                {"import_path": "logic_adapters.vector_logic_adapter.VectorLogicAdapter"},
                # {"import_path": "logic_adapters.time_logic_adapter.TimeLogicAdapter"}

            ],
            database="./database.json",
            read_only=True  # don't train bot with user data
        )
        self.__train()

    def answer(self,text):
        print("")
        print("Question",text)
        self.chatbot.question = Question(text)
        self.chatbot.question.show()
        print("\nAnswering..")
        rawResponse = self.chatbot.get_response(text).text
        return self.__processResponse(rawResponse)

    def __train(self):
        return
        from chatterbot.trainers import ListTrainer
        import conversation_helper

        conversations = conversation_helper.importConversations("./conversation_data/questions.txt")
        print("Training..",len(conversations))
        self.chatbot.set_trainer(ListTrainer)
        counter = 0
        for c in conversations:
            print(counter)
            counter += 1
            self.chatbot.train(c)
        print("Training End!")

    def __processResponse(self,response):
        import re
        for p in re.findall("(<[^<>]*>)", response):
            print(p)
            response = response.replace(p,self.chatbot.question.getInformation(p))
        return response


