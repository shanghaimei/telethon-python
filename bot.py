import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import json
import requests
from telethon.tl.custom import Button
from telethon import events
from telethon import TelegramClient

bot = telegram.Bot(token = 'your token')
updater = Updater(token='your token')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
print(bot.get_me())

def command(handler,cmd=None,**kw):
    def decorater(func):
        def wrapper(*args,**kw):
            return func(*args,**kw)
        if cmd==None:
            func_hander=handler(func,**kw)
        else:
            func_hander=handler(cmd,func,**kw)
        dispatcher.add_handler(func_hander)
        return wrapper
    return decorater


#/welcome 欢迎语
@command(CommandHandler,'welcome')
def welcome(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='''✨Welcome to <a href="https://t.me/haimei_group">BiBi's group</a> chat {} !'''.format(update.message.from_user.first_name) ,parse_mode="html" )

#帮助  /start
@command(CommandHandler,'start')
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="<pre>Hello {},😘I'm Haimei_bot ～\nyou can choose:</pre>\n/start - help \n/id - View the current chat_id \n/google - search".format(update.message.from_user.first_name),reply_to_message_id = update.message.message_id, parse_mode="html")
# chat_handler = CommandHandler('chat', chat)
# dispatcher.add_handler(chat_handler

#、/google 搜索
@command(CommandHandler,'google')
def google(bot,update):
    bot.send_message(
    chat_id=update.message.chat_id,       
    text="<pre>search</pre>",   
    reply_markup={             
    "inline_keyboard": [[{      
        "text":"google",            
        "url":"www.google.com",
         }]],
    },
    reply_to_message_id = update.message.message_id,
    parse_mode="html"      
    ) 


#获取群chat_id   /id
@command(CommandHandler,'id')
def id(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="<pre>chat_id is ：{}</pre>".format(str(update.message.chat_id)),reply_to_message_id = update.message.message_id,parse_mode="html")


#获取自己的上一条记录  /uptext
# @command(CommandHandler,'uptext')
# def uptext(bot,update):
#     bot.send_message(chat_id =update.message.chat_id,text="您的上一条记录是： "+ update.message.text)

#获取自己的详细信息




#获取特定的经纬度，由机器人发送给用户，作用：可用于获取公司地址
# @command(CommandHandler,'uptext')
# def uptext(bot,update):
#     bot.send_location(chat_id =update.message.chat_id,latitude=63.23,longitude=26.133,disable_notification = False)



#都回复hello
# @command(MessageHandler,Filters.text)
# def echo(bot, update,KeyboardButton):
#     bot.send_message(chat_id=update.message.chat_id, text='hello')
# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)


    #获取管理员信息
    # members=bot.get_chat_administrators(update.message.chat.id)
    # for member in members:
    #     print(member)
    #获取成员个数
    # print(bot.get_chat_members_count(update.message.chat.id))


@command(CommandHandler,'caps',pass_args=True)
def caps(bot, update, args):
    text_caps = ' '.join(args).upper() 
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


@command(InlineQueryHandler)
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


@command(MessageHandler,Filters.command)
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="<pre>Sorry, I didn't understand that command.\nyou can choose:</pre>\n/start - help \n/id - View the current chat_id \n/google - search",reply_to_message_id = update.message.message_id,parse_mode="html")


@command(CommandHandler,'reply')
def reply(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)



updater.start_polling()
# updater.stop()
