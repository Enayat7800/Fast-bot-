from pyrogram import client,idle
from pyrogram import filters

api_id = 28150346
api_hash = "426f0d0a1da02dea8fb71cb0bd3ab7e1"
bot_token = "6611439999:AAEDykIF7TG7aaRXLSwDXIqhvBm1Z6XEN74"


app = client(
  name = "enayatali",
  api_id = api_id,
  api_hash = api_hash,
  bot_token = bot_token,
)

@bot.message_handler(['help'])
def help(message) :
    bot.reply_to(message, "feel free to use as a calculator. If you want any help please contect to @Enayatali1 ")

app.start()
print("hello how are you")
idle()
