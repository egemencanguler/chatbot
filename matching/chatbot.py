

class Chatbot:
    def __init__(self):
        from chatterbot import ChatBot
        self.chatbot = ChatBot(
            "HÜBOT",
            storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch",
                # "chatterbot.logic.MathematicalEvaluation",
                # {"import_path": "logic_adapters.email_logic_adapter.EmailLogicAdapter"},
                # {"import_path": "logic_adapters.time_logic_adapter.TimeLogicAdapter"}

            ],
            database="./database.json",
            read_only=True  # don't train bot with user data
        )

        self.__train()

    def answer(self,question):
        return self.chatbot.get_response(question.raw)

    def __train(self):
        from chatterbot.trainers import ListTrainer
        import conversation_helper

        faqs = conversation_helper.importConversations("./conversation_data/faqs.txt")
        greetings = conversation_helper.importConversations("./conversation_data/greetings.txt")
        building = conversation_helper.importConversations("./conversation_data/building.txt")
        mail = conversation_helper.importConversations("./conversation_data/mail.txt")
        conversations = faqs + greetings + building + mail

        self.chatbot.set_trainer(ListTrainer)
        for c in conversations:
            self.chatbot.train(c)