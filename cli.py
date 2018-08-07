from telethon import TelegramClient, sync,events
import logging
import random
import asyncio
import telethon
from telethon.tl.types import PeerUser, PeerChat, PeerChannel,UpdateNewChannelMessage
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon import utils
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
import time
from telethon.errors import UserPrivacyRestrictedError


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.debug('Debug messages')
logger.info('Useful information')
logger.warning('This is a warning!')

api_id = 381462
api_hash = '63d2a1ad012aadb203312c405529cc8a'
client = TelegramClient('@shanghaimei', api_id, api_hash).start()
#给自己发送一条信息
# client.send_message('me', 'Hello! Talking to you from Telethon')
# client.send_file('me', '/home/shanghaimei/Pictures/images.png')

#获取上一条信息
# messages = client.get_messages('china_BiBi')
# print(messages[0].text)

#chat
# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         await event.reply('hi!')
#     if 'what' and 'name' in event.raw_text:
#         await event.reply('Haimei_bot,Thanks!')

#自动回复重复语句
# def replier(update):
#     if isinstance(update, UpdateNewChannelMessage) and update.message.reply_to_msg_id is None:
#         client.send_message(update.message.to_id, 'test', reply_to=update.message.id)

#朱铭id信息
# peer = client.get_input_entity('@HuingZM')
# peer = utils.get_input_peer(peer)
# print(peer)
# InputPeerUser(user_id=585015279, access_hash=-5271068656468837484)

#给朱铭和频道发送信息
# result = client(SendMessageRequest('HuingZM', 'Hello there!'))
# result = client(SendMessageRequest(PeerChannel(1182116619), 'Hello there!'))
# print(result)


# dialogs = client.get_dialogs()
# 打印群信息
# print(client.get_entity("@hello"))

#打印频道信息
# my_channel = client.get_entity(dialog.title)
# print(my_channel)

#检索个人的全部信息
# from telethon.tl.functions.users import GetFullUserRequest
# full = client(GetFullUserRequest('HuingZM'))
# print(full)


#过滤频道,获取频道成员
# telethon.errors.rpcerrorlist.UserPrivacyRestrictedError: The user's privacy settings do not allow you to do this
# for dialog in client.iter_dialogs():
#     friend_info = client.get_entity(dialog.title) #dialog.title为first_name
#     if type(friend_info) is not telethon.tl.types.User:
#         channel_id = friend_info.id
#         channel_title = friend_info.title
#         channel_username = friend_info.username
#         dict_channel_info = {"channel_id":channel_id,"channel_title":channel_title,"channel_username":channel_username}
#         # print(dialog.title,"这是一个频道",dict_channel_info)
#         channel = client.get_entity(PeerChannel(channel_id))  # 根据群组id获取群组对
#         responses = client.iter_participants(channel, aggressive=True) # 获取群组所有用户信息
#         for response in responses:
#             if response.username is not None:
#                 d = {'id':response.id,'username':response.username}
#                 print(d)
#                 time.sleep(2)
#                 client(InviteToChannelRequest(
#                 channel=1219921340,
#                 users = [d.get('username')],
#                 ))
#                 client.send_message(1219921340,'''✨Welcome to <a href="https://t.me/haimei_group">BiBi's group</a> chat {} !'''.format(d.get('username')) ,parse_mode="html")
#                 time.sleep(2)
 




#邀请成员进入频道,加机器人可以，加朱铭不可以,用户的隐私不允许你这样做
# client(InviteToChannelRequest(
#     channel= 1219921340,
#     users = ['HuingZM'],
#     ))



#转发信息
# messages = client.get_messages('china_BiBi')
# print(messages[0])
# mes_id = messages[0].id
# mes_text = messages[0].text
# print(mes_text)
# client.forward_messages(1219921340,mes_id,1182116619)

messages = client.get_messages('china_BiBi')
mes_id_1 = messages[0].id
while True:
    messages = client.get_messages('china_BiBi')
    mes_id = messages[0].id
    if mes_id != mes_id_1:
        client.forward_messages(1219921340,mes_id,1182116619)
        mes_id_1 = mes_id




# For normal chats
# client(AddChatUserRequest(
#     chat_id = -1001219921340 , #chat_id
#     user_id = 585015279, #被邀请人id
#     fwd_limit=10  # Allow the user to see the 10 last messages
# ))


#获取全部的聊天信息
# for message in client.iter_messages(1182116619):
#     ms_id = message.id
#     print(ms_id)

#变量chat为频道id
# chat =[1182116619,-26944244] 列表不支持  
# for user in client.iter_participants(596848869):
#     dialogs  = client.get_dialogs()
#     print(dialogs) #聊天列表
#     first = dialogs[1]
#     print(first.title)


#获取EOS频道的成员信息
# 1142634987
# channel = client.get_entity(PeerChannel(1387666944))  # 根据群组id获取群组对象
# responses = client.iter_participants(channel, aggressive=True) # 获取群组所有用户信息
# for response in responses:
#     if response.username is not None:
#         d = {'id':response.id,'username':response.username}
#         print(d)

# channel = 1182116619
# from telethon.tl.functions.channels import InviteToChannelRequest
# client(InviteToChannelRequest(
#     channel

# ))

async def main():
    await client.run_until_disconnected()



if __name__=='__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())










    