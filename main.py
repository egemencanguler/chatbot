from chatterbot import ChatBot
import logging

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "HÜBOT",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        # "chatterbot.logic.MathematicalEvaluation",
        {"import_path": "email_logic_adapter.EmailLogicAdapter"},
        {"import_path": "time_logic_adapter.TimeLogicAdapter"}

    ],
    database="./database.json",
    read_only= True # don't train bot with user data
)

from chatterbot.trainers import ListTrainer

import conversation_helper
conversations = conversation_helper.importConversations("./faqs.txt")

chatbot.set_trainer(ListTrainer)
for c in conversations:
    chatbot.train(c)

while True:
    try:
        response = chatbot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break




