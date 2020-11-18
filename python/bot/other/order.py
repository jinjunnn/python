# 把中奖页面的

import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "IGXFL8L08BMSNVGLyGhWr74I-gzGzoHsz", master_key="kOzll9KspLj58V55JhtM1Udv")

listName = 'Other'  #在这里写入表的名称
key = 'authData'  #在这里写入修改字段的名称
value = {}  #在这里写入需要修改字段的值的名称
for i in range(1, 6):
    query = leancloud.Query(listName)
    query.not_equal_to(key, value)
    # 在这里可以配置更多的查询条件
    query.limit(1000)

    for item in query.find():
        Lottery = leancloud.Object.extend(listName)
        lottery = Lottery.create_without_data(item.id)
        lottery.set(key, value)
        lottery.save()