from roll_witch import bot
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World"


if __name__ == '__main__':
    bot_thread = Thread(target=bot.start_bot, name='discord-bot-thread', daemon=True)
    bot_thread.start()
    app.run(host='127.0.0.1', port=8080, debug=True)
