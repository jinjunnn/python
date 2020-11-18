# LotteryToday 中的抽奖用户，部分修改为中奖用户。

import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "IGXFL8L08BMSNVGLyGhWr74I-gzGzoHsz", master_key="kOzll9KspLj58V55JhtM1Udv")

t = 0
list = []
# 设置开始的日期，因为中奖名单只有10个人，所以可以一次遍历完所有，不需要去设置时间。
# 设置需要开奖的起止时间，去做查询。

Lottery = leancloud.Object.extend('Lottery')
query1 = Lottery.query
query2 = Lottery.query
query1.greater_than_or_equal_to('deadline', datetime(2019, 2, 1))
query2.less_than('deadline', datetime(2019, 3, 1))
query = leancloud.Query.and_(query1, query2)


query.limit(400)
print(query.count())

for item in query.find():
    print(item.id)

    # 这段代码是向lottery表中的openlotteryget字段改为TURE，目的是为了说明这个抽奖已经开奖完成了。
    Lottery = leancloud.Object.extend('Lottery')
    lottery = Lottery.create_without_data(item.id)
    lottery.set('openLotteryGet', True)
    lottery.save()

    # 通过“targetLottery”字段查询lotterytoday表
    query = leancloud.Query('LotteryToday')
    query.equal_to("targetLottery", lottery)
    query.limit(1000)
    query_list = query.find()
    query_count = query.count()

    for item in range(1, 11):
        try:
            num = 0
            if query_count >= 1000:
                num = random.randint(0, 1000)
            else:
                num = random.randint(0, query_count)
            print(num)

            LotteryToday = leancloud.Object.extend('LotteryToday')
            lotteryToday = LotteryToday.create_without_data(query_list[num].id)
            lotteryToday.set('get', True)
            lotteryToday.save()
        except:
            pass
