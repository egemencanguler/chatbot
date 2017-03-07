from chatterbot import ChatBot
from preprocessor import Preprocessor
from postprocessor import Postprocessor
from information import InformationManager

import logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "HÜBOT",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        # "chatterbot.logic.MathematicalEvaluation",
        {"import_path": "logic_adapters.email_logic_adapter.EmailLogicAdapter"},
        # {"import_path": "logic_adapters.time_logic_adapter.TimeLogicAdapter"}

    ],
    database="./database.json",
    read_only= True # don't train bot with user data
)

preprocessor = Preprocessor()
postprocessor = Postprocessor()

from chatterbot.trainers import ListTrainer

import conversation_helper
conversations = []
faqs = conversation_helper.importConversations("./conversation_data/faqs.txt")
greetings = conversation_helper.importConversations("./conversation_data/greetings.txt")
building = conversation_helper.importConversations("./conversation_data/building.txt")
conversations = faqs + greetings + building

chatbot.set_trainer(ListTrainer)
for c in conversations:
    chatbot.train(c)

while True:
    userStatement = input()
    statement = preprocessor.process(userStatement)
    print("Statement: ", statement)
    response = chatbot.get_response(statement)
    response = postprocessor.process(response.text)
    print(response)


