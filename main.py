import telebot, os
from telebot.types import InlineKeyboardMarkup as ikm
from telebot.types import InlineKeyboardButton as ikb
from time import sleep
from gasfees import gasfee, uniswap, erc20
from alive import keep_alive
from ethprice import getprice

keep_alive() #This function is used to keep the bot alive on replit server

Token = os.environ["token"] #This is bot's API Token

bot = telebot.TeleBot(Token, parse_mode="HTML")

print("Bot started successfully! Running Now...")

knwn = [ ]
with open('userids.txt', 'r') as uids:
 knwn = uids.read()
knwn = knwn.split()

wlcm = """Ciao! I'm ETH Gas Fee Tracker Bot, I can send you live Ethereum Gas Fees in GWEI & USD.

Send /gas to see!
All Commands - /cmds

Donate to support the development of this bot: /donate
"""

donate = """Donate to support the development of this bot:
<b>Blockchain Domain:</b> <a href="https://advik.click/ud">advik.wallet</a>
<b>Donate with</b> <a href="https://advik.click/nano-donate">Nano</a>

Thanks a ton!
"""

cmds = """<b><ins>All Commands:</ins></b>
/gas - See live gas fee
/uni - Check live Uniswap V3 & V2 gas fees
/erc20 - Check live ERC-20 Token's transfer fees
/p - Get Ethereum Live Price
/donate - Donate to support development of this bot
/contact - Contact my Dev regarding anything

<b>Check Bot Uptime:</b> https://bots.advik.dev/
"""


@bot.message_handler(commands=["start", "home"])
def wlcmsg(msg):
    chatid = str(msg.chat.id)
    mrkp = ikm()
    mrkp.add(ikb("Join Channel For Updates", url="https://t.me/DevUpdate"))
    if chatid not in knwn: #This is used to determine new users using the bot
        knwn.append(chatid)
        with open('userids.txt', 'w') as uids:
            for uid in knwn:
                uid = uid + ' '
                uids.write(uid)
    bot.send_message(msg.chat.id, wlcm, reply_markup=mrkp, disable_web_page_preview=True)
	

@bot.message_handler(commands=["gas"])
def ethgas(msg):
    bot.send_message(msg.chat.id, gasfee(), disable_web_page_preview=True)
    chatid = str(msg.chat.id)
    if chatid not in knwn:
        knwn.append(chatid)
        with open('userids.txt', 'w') as uids:
            for uid in knwn:
                uid = uid + ' '
                uids.write(uid)

@bot.message_handler(commands=['uni', 'uniswap'])
def unigas(msg):
    bot.send_message(msg.chat.id, uniswap(), disable_web_page_preview=True)
    chatid = str(msg.chat.id)
    if chatid not in knwn:
        knwn.append(chatid)
        with open('userids.txt', 'w') as uids:
            for uid in knwn:
                uid = uid + ' '
                uids.write(uid)

@bot.message_handler(commands=['erc', 'erc20'])
def ercfees(msg):
    bot.send_message(msg.chat.id, erc20(), disable_web_page_preview=True)
    chatid = str(msg.chat.id)
    if chatid not in knwn:
        knwn.append(chatid)
        with open('userids.txt', 'w') as uids:
            for uid in knwn:
                uid = uid + ' '
                uids.write(uid)
		
@bot.message_handler(commands=["donate"])
def donateme(msg):
	bot.send_message(msg.chat.id, donate, disable_web_page_preview=True)

		
@bot.message_handler(commands=["contact"])
def pingme(msg):
	mrkp = ikm() #Created InlineKeyboardMarkup
	mrkp.add(ikb("Telegram", url="https://t.me/ETHGasFeeSupportBot"), ikb("Email", url="https://advik.click/ETHBot/")) #Added URLs to markup
	mrkp.add(ikb("Join Channel For Updates", url="https://t.me/DevUpdate"))
	bot.send_message(msg.chat.id, "Ping me if you've any query or want some new features:", reply_markup=mrkp)

		
@bot.message_handler(commands=["cmd", "cmds"])
def cmd(msg):
	bot.send_message(msg.chat.id, cmds, disable_web_page_preview=True)

   
#Hehe
@bot.message_handler(commands=["dev"])
def iownit(msg):
    bot.reply_to(msg, "Made by @DevAdvik")


@bot.message_handler(commands=["p"])
def usdbtc(msg):
    if len(msg.text) == 2 or msg.text.lower() == '/p@ethgasfeetrackerbot':
    	bot.send_message(msg.chat.id, getprice(), disable_web_page_preview=True)


#Function to get list of all user IDs, can only be used by me
@bot.message_handler(commands=["uid", "uids"])
def getuid(msg):
    if msg.chat.id == my_user_id:
        users = open("userids.txt", "rb")
        bot.send_document(my_user_id, users)
        users.close()
    else:
        bot.send_message(msg.chat.id, "Error, You're an unauthorized user!")

	
#Not for common users, this function is used to send mesages to users using the bot, like announcement messages, etc.
#Can only be used by the given user id, in this case, by me
@bot.message_handler(commands=['send'])
def sendnotif(msg):
    if msg.chat.id == my_user_id:
        confirm = bot.send_message(msg.chat.id, "Send the message you'd like to be notified:")
        bot.register_next_step_handler(confirm, msgpreview)
    else:
        bot.reply_to(msg, "You're not allowed to use this command!")

def msgpreview(msg):
    global msgpre
    msgpre = msg.text
    confirmit = bot.send_message(msg.chat.id, f"{msgpre}\n-\nThis is the message. Are you sure you want to send it?", disable_web_page_preview=True)
    bot.register_next_step_handler(confirmit, sendit)

def sendit(msg):
    try:
        if msg.text.lower() == "yes" or msg.text.lower() =="y":
            allusers = 0
            for uid in knwn:
                try:
                    userid = int(uid)
                    bot.send_message(userid, msgpre, disable_web_page_preview=True)
                    sleep(0.04)
                    allusers+=1
                except:
                    sleep(0.04)
        bot.send_message(my_user_id, f"Message has been sent to {allusers} users!")
    except:
        bot.send_message(my_user_id, "Message sending cancelled!")

	
#Function to check the number of active users using the bot, is kinda buggy, but works the second time:/
#This too can only be used by given user id, i.e., by me
@bot.message_handler(commands=["active"])
def countactive(msg):
    actv=0
    if msg.chat.id == my_user_id:
        for uid in knwn:
            try:
                userid = int(uid)
                bot.send_chat_action(userid, "typing")
                sleep(0.04)
                actv+=1
                iopo = actv #For some fcking reason, if I don't include this line, the function breaks
            except:
                knwn.remove(uid)
                sleep(0.04)
        bot.send_message(my_user_id, f"No. of active users: {iopo}")
        with open('userids.txt', 'w') as uids:
            for uid in knwn:
                uid = uid + ' '
                uids.write(uid)
    else:
        bot.reply_to(msg, "Unauthorised User: You don't have access to this command!")


while True:
	try:
		bot.infinity_polling(skip_pending=True)
		telebot.apihelper.SESSION_TIME_TO_LIVE = 2400
	except:
		sleep(1)
