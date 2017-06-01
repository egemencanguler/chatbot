from chatbot.chatbot import Chatbot
bot = Chatbot()
while True:
    print("Response: ", bot.answer(input()))