from notifiers import get_notifier
def make_telegram_notifier(
        token='6172070577:AAGERfg9Cqv2vF6UN_NDs2AY9-mGsjR3e8U',
        chat_id=462441070):
    def f(text):
        telegram = get_notifier('telegram')
        telegram.notify(message=text,
                        token=token,
                        chat_id=chat_id)
    return f

send = make_telegram_notifier()
send("Hou are you?")