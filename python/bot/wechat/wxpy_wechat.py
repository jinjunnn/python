# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

bot.enable_puid('wxpy_puid.pkl')
friends = bot.friends()

for item in friends:
    if item.puid:
        print(item.puid)
    if item.alias:
        print(item.alias)
    if item.uin:
        print(item.uin)
    if item.wxid:
        print(item.wxid)
    if item.user_name:
        print(item.user_name)
    