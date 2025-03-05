from typing import final
from  telegram import Update
from  telegram.ext import Application, CommandHandler, MessageHandler, filters,ContextTypes

TOKEN: final = "5401619222:AAGK7MWUB8IzxhLyyYUuiYoX-JDDSuCljPY"
USERNAME: final = "@klaipeda_molas_kite_bot"

# Commands
async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("Hello! I'm a bot for freedive coaching.")

async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text("help")

async def custom_command(update: Update, context: ContextTypes):
    await update.message.reply_text("custom")

#Responceses

def handle_response(text: str) -> str:
    processsed_text = text.lower()
    if "hello" in processsed_text:
        return "Hello! I'm a bot for freedive coaching?"

    return "I don't understand you"
async def handle_message(update: Update, context: ContextTypes):
    message_type = update.message.chat.type
    print(f'message_type: {message_type}')
    if message_type == "private":
        response = handle_response(update.message.text)
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("I can only talk in private chats")

async def error(update: Update, context: ContextTypes):
    await update.message.reply_text("An error occured")

# Main runner
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    #COMMANDS (need to be added first in bot father)
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    #MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #ERRORS
    app.add_error_handler(error)


    #CHECK messages every 5 seconds
    print("polling...")
    app.run_polling(poll_interval=5)