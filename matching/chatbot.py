

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
                # ,
                # {"import_path": "logic_adapters.vector_logic_adapter.VectorLogicAdapter"},
                # "chatterbot.logic.MathematicalEvaluation",
                {"import_path": "logic_adapters.vector_logic_adapter.VectorLogicAdapter"},
                # {"import_path": "logic_adapters.time_logic_adapter.TimeLogicAdapter"}

            ],
            database="./database.json",
            read_only=True  # don't train bot with user data
        )

        self.__train()

    def answer(self,question):
        return self.chatbot.get_response(question)

    def __train(self):
        from chatterbot.trainers import ListTrainer
        import conversation_helper

        # faqs = conversation_helper.importConversations("./conversation_data/faqs.txt")
        greetings = conversation_helper.importConversations("./conversation_data/greetings.txt")
        building = conversation_helper.importConversations("./conversation_data/building.txt")
        mail = conversation_helper.importConversations("./conversation_data/mail.txt")
        questions = conversation_helper.importConversations("./conversation_data/questions.txt")
        conversations = greetings + building + mail + questions

        self.chatbot.set_trainer(ListTrainer)
        for c in conversations:
            self.chatbot.train(c)