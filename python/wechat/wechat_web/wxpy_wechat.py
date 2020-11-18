# 导入模块
import time
from wxpy import *
import leancloud
from leancloud import cloudfunc
import common
import _thread
import csv

file_card = open('wechat/wechat_web/resource/card.csv', 'a')
file_goods = open('wechat/wechat_web/resource/goods.csv', 'a')
file_message = open('wechat/wechat_web/resource/message.csv', 'a')

card = csv.writer(file_card)  #创建写的对象
goods = csv.writer(file_goods)  #创建写的对象
message = csv.writer(file_message)  #创建写的对象

leancloud.init("XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")
bot = Bot()

minute = 5

bot.enable_puid('wxpy_puid.pkl')
friends = bot.friends()
groups = bot.groups()


# 自动发消息的群
# group1 = bot.groups().search(group_name1)
# group2 = bot.groups().search(group_name2)
# group3 = bot.groups().search(group_name3)
# group4 = bot.groups().search(group_name4)
# group5 = bot.groups().search(group_name5)
# group6 = bot.groups().search(group_name6)


header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
}

#  自动发送消息
# def sd_msg():
#     if len(group1):
#         group1[0].send(msg1)
#         print(msg1,'已发送')
#     else:
#         print('未搜索到第1个群名')
#     if len(group2):
#         group2[0].send(msg2)
#         print(msg2, '已发送')
#     else:
#         print('未搜索到第2个群名')
#     if len(group3):
#         group3[0].send(msg1)
#         print(msg3, '已发送')
#     else:
#         print('未搜索到第3个群名')
#     if len(group4):
#         group4[0].send(msg2)
#         print(msg4, '已发送')
#     else:
#         print('未搜索到第4个群名')
#     if len(group5):
#         group5[0].send(msg1)
#         print(msg5, '已发送')
#     else:
#         print('未搜索到第5个群名')
#     if len(group6):
#         group6[0].send(msg6)
#         print(msg6, '已发送')
#     else:
#         print('未搜索到第6个群名')
#     time.sleep(minute*60)

@bot.register(friends, TEXT,False)
def print_friend_msg(msg):
    _thread.start_new_thread(common.rcv_msg,(msg.sender.puid, None, msg.sender.puid,msg.sender.name, msg.text, message))
    _thread.start_new_thread(common.get_card_info, (msg.text, card))
    _thread.start_new_thread(common.get_goods_info, (msg.text, goods))
    print(msg.text)


@bot.register(groups, TEXT,False)
def print_group_msg(msg):
    _thread.start_new_thread(common.rcv_msg, (msg.sender.puid, msg.sender.name, msg.sender.puid,msg.sender.name, msg.text, message))
    _thread.start_new_thread(common.get_card_info, (msg.text, card))
    _thread.start_new_thread(common.get_goods_info, (msg.text, goods))
    print(msg.text)

# @bot.register(friends, PICTURE,False)
# def print_friend_image_msg(msg):
#     file = leancloud.File(msg.file_name, msg.get_file())
#     file.save()
#     _thread.start_new_thread(common.rcv_msg,(msg.sender.puid, None, msg.sender.puid, msg.sender.name, msg.file_name,message)

# @bot.register(groups, PICTURE, False)
# def print_group_image_msg(msg):
#     file = leancloud.File(msg.file_name, msg.get_file())
#     file.save()
#     _thread.start_new_thread(common.rcv_msg,(msg.receiver.puid, msg.receiver.name, msg.sender.puid, msg.sender.name, msg.file_name,message))

embed()
