import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc
# # SUGAR 项目
# leancloud.init("XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

#  其他  项目  选择需要发送模板消息的后台
leancloud.init("0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")

programid = 2  #设置要发模板消息的小程序 2 抽奖

#   即将开奖通知
data1 = {
    'touser': '',
    'template_id': 'k2_YJUliPs0h1SyNa2u1IUP4hJWE2pJkv8S0t1Uyx7k',
    'page': '/pages/user/record/record',
    'data': {
        'thing1': {
            'value': '丝芙兰100美金礼品卡',
        },
        'date3': {
            'value': '2019年11月18日',
        },
        'thing4': {
            'value': '汇率4.90，卡商微信:xxxxxxxx',
        }
    },
}
#   中奖结果通知
data2 = {
    'touser': '',
    'template_id': 'qPdhctZF31bJcXr4gqLrFbsVhXXFYBY3MCFjxZ5H4fQ',
    'page': '/pages/wish/wish',
    'data': {
        'thing6': {
            'value': '奖品中国电信50元充值卡',
        },
        'character_string2': {
            'value': '49424',
        },
        'thing9': {
            'value': '恭喜您中奖！',
        },
        'thing10': {
            'value': '请您登陆小程序领取奖励。',
        }
    },
}


def print_result():
    #打印发送结果  csv  了解发送成功了多少，失败了多少。
    pass


def send_subscribe_message(objectid,message):
    data = message
    data['touser'] = objectid
    ge = cloudfunc.run('send_subscribe_message',data=json.dumps(data),programid=programid)
    print(ge)


send_subscribe_message(
    'o56y35QoNPk7VKSYQdMJ-M33P0P0',
    data2)
#   查询用户
# def query_users():
#     key = 'user_o56y35*' # 这个是抽奖小程序
#     users = cloudfunc.run('keys',key=key)
#     for user_key in users:
#         user = cloudfunc.run('getHash', key=user_key)
#         send_subscribe_message(user['objectid'], user['uid'])

# query_users()

# 查询所有用户
# ge = cloudfunc.run('keys', key='user_*')
# for item in ge:
#     user = cloudfunc.run('getHash', key=item)
#     print(
#         user.get('uid', ''), user.get('nickName', ''), user.get(
#             'f_balance', ''), user.get('image', ''))