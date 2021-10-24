import telebot
from telebot.types import InlineKeyboardMarkup as ikm
from telebot.types import InlineKeyboardButton as ikb
from time import sleep
from gasfees import gasfee

Token = "Bot_Access_Token"

bot = telebot.TeleBot(Token, parse_mode="HTML")

print("Bot started successfully! Running Now...")

wlcm = """Ciao! I'm ETH Gas Fee Tracker Bot, I can send you live Ethereum Gas Fees in GWEI.

Send /gas to see!

All Commands - /cmd
"""

donate = """I don't cost any money but I do have some running costs. My developer will be very grateful if you donate any amount of crypto to support the development of this bot!

<b><ins>Addresses:</ins></b>

<i>Ethereum/Matic:</i> <code>0xA28CAb9DFb91078d3E2508F322c4f816c7c851c4</code>

<i>Bitcoin:</i> <code>bc1q6f0gvamlxpq0qxze4qkj83vpf0f764eefcu7dq</code>

<i>Dogecoin:</i> <code>DQB9XgyGR5Dv9AVWHF1iJF8ewBMTGxvcEq</code>

<i>Litecoin:</i> <code>ltc1qxqymjgkv2xulz2a5rsync5ea0hgxeuvzegfzuf</code>

<i>Monero:</i> <code>42wtBJDKg1bJSqpfFgXnzM2gJeB19Ztzj7UmYrAHJfKu4BZVgMsXwKvBw9TyGPwHN8AcqAByXpRSz73TfJeytLhMTku2fTk</code>


After donating, please send a screenshot of donation you sent to @ETHGasFeeSupportBot. Thanks!
"""

cmds = """<b><ins>All Commands:</ins></b>
/gas - See live gas fee
/donate - Donate to support development of this bot
/contact - Contact my Dev regarding anything
"""

@bot.message_handler(commands=["start", "home"])
def homie(msg):
	bot.send_message(msg.chat.id, wlcm)
	

@bot.message_handler(commands=["gas"])
def ethgas(msg):
	bot.send_message(msg.chat.id, gasfee(), disable_web_page_preview=True)

		
@bot.message_handler(commands=["donate"])
def donateme(msg):
	bot.send_message(msg.chat.id, donate)

		
@bot.message_handler(commands=["contact"])
def pingme(msg):
	mrkp = ikm()
	mrkp.add(ikb("Telegram", url="https://t.me/ETHGasFeeSupportBot"), ikb("Email", url="https://u.advik.dev/ETHBot/"))
	
	bot.send_message(msg.chat.id, "Ping me if you've any query or want some new features:", reply_markup=mrkp)

		
@bot.message_handler(commands=["cmd", "cmds"])
def cmd(msg):
	bot.send_message(msg.chat.id, cmds)



while True:
	try:
		bot.polling(0.04)
		telebot.apihelper.SESSION_TIME_TO_LIVE = 2000
	except:
		sleep(1)