from matching.chatbot import Chatbot
bot = Chatbot()

while True:
    text = input()
    response = bot.answer(text)
    print("Response:",response)

