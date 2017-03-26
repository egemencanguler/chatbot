# from matching.chatbot import Chatbot
#
# bot = Chatbot()
#
#
# from containers.question import Question
# from preprocessing.preprocessor import Preprocessor
#
# preprocessor = Preprocessor()
# while True:
#     raw = input()
#     question = Question(raw)
#     question = preprocessor.process(question)
#     print(question)
#
#     # statement = preprocessor.process(userStatement)
#     # print("Statement: ", statement)
#     # response = chatbot.get_response(statement)
#     # response = postprocessor.process(response.text)
#     # print("Response:",response)

from database.database import DataBase
db = DataBase()
print("hoo")
vec = db.getVector("merhabalar")
print(vec)
