# LotteryToday 中的抽奖用户，部分修改为中奖用户。

import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "IGXFL8L08BMSNVGLyGhWr74I-gzGzoHsz", master_key="kOzll9KspLj58V55JhtM1Udv")

skip_user = 0
list = []
# 设置开始的日期，因为中奖名单只有10个人，所以可以一次遍历完所有，不需要去设置时间。
# reminder1 = datetime(2018, 11, 16, 00, 00, 00)
query = leancloud.Query('Property')
query.limit(1000)
query_list = query.find()

for item in query.find():
    # 这个道具一共有多少人中奖
    objectId = item.id
    num_get = item.get('timesGet')
    content = item.get('title') + item.get('content')
    query = leancloud.Query('LotteryGet')
    Property = leancloud.Object.extend('Property')
    property = Property.create_without_data(objectId)
    query.equal_to('targetProperty', property)
    lottery_get_amount = query.count()
    print(num_get)
    print(lottery_get_amount)
    print(content)

    if lottery_get_amount < num_get:
        query = leancloud.Query('_User')
        query.exists('userName')
        query.exists('userImage')
        if (num_get - lottery_get_amount) > 1000:
            query.limit(1000)
        else:
            query.limit(num_get - lottery_get_amount)
        query.skip(23000 + num_get - lottery_get_amount)
        for item in query.find():
            LotteryGet = leancloud.Object.extend('LotteryGet')
            _User = leancloud.Object.extend('_User')
            Property = leancloud.Object.extend('Property')
            lotteryGet = LotteryGet()
            lotteryGet.set('get', False)
            lotteryGet.set('property', content)
            lotteryGet.set('realUser', False)
            lotteryGet.set('paid', True)
            lotteryGet.set('targetUser', _User.create_without_data(item.id))
            lotteryGet.set('targetProperty',
                           Property.create_without_data(objectId))
            list.append(lotteryGet)
        LotteryGet.save_all(list)
        list.clear()
        print(list)
        skip_user = skip_user + num_get - lottery_get_amount
    else:
        pass