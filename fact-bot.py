import requests,logging
from telegram import Update
from telegram.ext import CommandHandler,ContextTypes,ApplicationBuilder

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def gen_fact():
    url=f'https://uselessfacts.jsph.pl/api/v2/facts/random'
    req=requests.get(url)
    # print(req.status_code)
    if req.status_code !=200:
        return f"Unknown Error\nStatus Code={req.status_code}"
    else:
        res=req.json()['text']
        return res

token=input("Enter Bot token: ").strip()

async def start(update: Update,context= ContextTypes.DEFAULT_TYPE):
    name=update.effective_chat.full_name
    username=update.effective_chat.username
    id=update.effective_chat.id
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""👋 Heyy {name}!

        🤖 Welcome to Telegram Bot

        📋 Your Info:
        👤 Username: @{username}
        🆔 Chat ID: {id}

        ✨ Enjoy your stay!
        🚀 Use /fact to get a random fact.
        """
    )
async def fact(update : Update, context: ContextTypes.DEFAULT_TYPE):
    fact=gen_fact()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Do You Know?\n\n{fact}'

    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler("start", start)
    fact_handler = CommandHandler("fact", fact)

    app.add_handler(start_handler)
    app.add_handler(fact_handler)

    app.run_polling()