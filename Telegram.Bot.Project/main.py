from telegram.ext import *
import key
import tracemalloc
tracemalloc.start()

print("start...")


def start_command(update, context):
    update.message.reply_text("hello. i am ready!")


def help_command(update, context):
    update.message.reply_text("ill try to help you with everything")


def user_responce_command(text: str) -> str:
    if "hello!" in text:
        return "hello there!"
    if "goodmorning" in text:
        return "goodmorning!!!"
    if "i need help" in text:
        return "tell me what you need !"
    if "how are you?" in text:
        return "im good! thx!"


def bot_responce_command(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    responce = ""

    if message_type == "group":
        if "@ProjectBot" in text:
            new_text = text.replace("@ProjectBot", '').strip()
            responce = user_responce_command(new_text)
    else:
        responce = user_responce_command(text)

    update.message.reply_text(responce)


def error_command(update, context):
    print(f"Update {update} caused error : {context.error}")


if __name__ == '__main__':
    updater = Updater(key.api_key, update_queue=True)
    dp = updater.Dispatcher
    # Run
    updater.start_polling()

