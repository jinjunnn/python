# LotteryToday 表中增加抽奖用户，目前有点问题，也就是微信不会持续化存储用户的头像信息。需要Leancloud主动存储用户的头像。

import leancloud
from datetime import datetime
import json

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

t = 0
list = []
# 设置开始的日期
reminder1 = datetime(2019, 2, 1, 00, 00, 00)
query = leancloud.Query('Lottery')
query.greater_than("deadline", reminder1)
query.equal_to("openLottery", False)
query.limit(28)
print(query.count())

for item in query.find():
    # 因为content和product已经被删除，需要链表查询Property表中的对应名。
    content = item.get('content')
    product = item.get('product')
    objectId = item.id
    Lottery = leancloud.Object.extend('Lottery')
    lottery = Lottery.create_without_data(item.id)
    lottery.set('openLottery', True)
    lottery.save()

    query = leancloud.Query('_User')
    query.exists('userName')
    query.exists('userImage')
    query.limit(209)
    query.skip(10000 + 209 * t)
    for item in query.find():
        LotteryToday = leancloud.Object.extend('LotteryToday')
        _User = leancloud.Object.extend('_User')
        Lottery = leancloud.Object.extend('Lottery')
        lotteryToday = LotteryToday()
        lotteryToday.set('get', False)
        lotteryToday.set('content', content)
        lotteryToday.set('product', product)
        lotteryToday.set('targetUser', _User.create_without_data(item.id))
        lotteryToday.set('targetLottery',
                         Lottery.create_without_data(objectId))
        list.append(lotteryToday)
    LotteryToday.save_all(list)
    list.clear()
    print(list)
    t = t + 1
