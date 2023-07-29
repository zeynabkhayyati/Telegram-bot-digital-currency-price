import telebot
import requests
TOKEN = "6097563643:AAHR4VnXJGgHMXrhKcMjBoOzk8hcozefBHI"
bot = telebot.TeleBot(TOKEN)
URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSTD"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(func=lambda m: True)
def show_price(message):
	symbol = message.text.upper()
	response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")

	if response.status_code == 200:
		data = response.json()
		bot.reply_to(message , f"{data['symbol']} price is {data['price']}")
	else:
		bot.reply_to(message , "This currency does not exist" )
    
	
	
bot.infinity_polling()
