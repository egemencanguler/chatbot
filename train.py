from chatbot.chatbot import Chatbot
bot = Chatbot()
bot.train("./conversation_data/questions.txt")
bot.answer("Cache")

