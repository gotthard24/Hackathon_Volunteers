from telegram.ext import Updater, CommandHandler

TOKEN = "7044408816:AAE-A9JwCxXjZkjuFRAXfE9cmx9AomdloP0"
def start(update, context):
    update.message.reply_text('Hello there')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    
def testing():
    pass
