from config import TOKEN, CHAT_ID
from time import ctime
from telepot import Bot


def make_sender(TOKEN, CHAT_ID):
    bot = Bot(TOKEN)
    def send(message=''):
        bot.sendMessage(CHAT_ID, message)
    return send


if __name__ == '__main__':
    send = make_sender(TOKEN, CHAT_ID)
    send(f'{ctime()} A minute has passed')
