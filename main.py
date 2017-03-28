from matching.chatbot import Chatbot
bot = Chatbot()

while True:
    question = input()
    response = bot.answer(question)
    print("Response:",response)

