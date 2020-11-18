# 导入模块
import time
from wxpy import *
import leancloud
from leancloud import cloudfunc
import text

leancloud.init("XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")
print(text.msg1)
bot = Bot()

minute = 5


bot.enable_puid('wxpy_puid.pkl')
friends = bot.friends()
groups = bot.groups()
time.sleep(30)

group1 = bot.groups().search(text.group_name1)
group2 = bot.groups().search(text.group_name2)
group3 = bot.groups().search(text.group_name3)
group4 = bot.groups().search(text.group_name4)
group5 = bot.groups().search(text.group_name5)
group6 = bot.groups().search(text.group_name6)


header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
}


def sd_msg():
    if len(group1):
        group1[0].send(text.msg1)
        print(text.msg1,'已发送')
    else:
        print('未搜索到第1个群名')
    if len(group2):
        group2[0].send(text.msg2)
        print(text.msg2, '已发送')
    else:
        print('未搜索到第2个群名')
    if len(group3):
        group3[0].send(text.msg3)
        print(text.msg3, '已发送')
    else:
        print('未搜索到第3个群名')
    if len(group4):
        group4[0].send(text.msg4)
        print(text.msg4, '已发送')
    else:
        print('未搜索到第4个群名')
    if len(group5):
        group5[0].send(text.msg5)
        print(text.msg5, '已发送')
    else:
        print('未搜索到第5个群名')
    if len(group6):
        group6[0].send(text.msg6)
        print(text.msg6, '已发送')
    else:
        print('未搜索到第6个群名')
    time.sleep(minute*60)


def rcv_msg(g, s, u, r, c):
    cloudfunc.run('rcv_msg', g=g,s=s,u=u,r=r,c=c)


@bot.register(friends, TEXT,False)
def print_friend_msg(msg):
    rcv_msg(msg.sender.puid, None, msg.sender.puid, msg.sender.name, msg.text)


@bot.register(groups, TEXT,False)
def print_group_msg(msg):
    rcv_msg(msg.receiver.puid, msg.receiver.name, msg.sender.puid, msg.sender.name, msg.text)


@bot.register(friends, PICTURE,False)
def print_friend_image_msg(msg):
    file = leancloud.File(msg.file_name, msg.get_file())
    file.save()
    rcv_msg(msg.sender.puid, None, msg.sender.puid, msg.sender.name, msg.file_name)


@bot.register(groups, PICTURE, False)
def print_group_image_msg(msg):
    file = leancloud.File(msg.file_name, msg.get_file())
    file.save()
    rcv_msg(msg.receiver.puid, msg.receiver.name, msg.sender.puid, msg.sender.name, msg.file_name)


if __name__ == "__main__":
    for i in range(1000):
        sd_msg()


embed()
