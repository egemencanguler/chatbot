from flask import Flask, render_template
from flask import request

from chatbot.chatbot import Chatbot
bot = Chatbot()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    question = request.form["question"]
    answer = bot.answer(question)
    return question + "</>" + answer

if __name__ == "__main__":
    app.run()
