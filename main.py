from matching.chatbot import Chatbot
bot = Chatbot()
# bot.train("./conversation_data/questions.txt")

while True:
    text = input()
    response = bot.answer(text)
    print("HÜBOT:",response)

