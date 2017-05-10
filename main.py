from matching.chatbot import Chatbot
bot = Chatbot()
bot.train("./conversation_data/questions.txt")
bot.answer("Cache")

