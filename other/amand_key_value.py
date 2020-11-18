# 修改某张表的某个字段值

import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "evYA8nbQwsUuU30S2UDt9UcI-gzGzoHsz", master_key="Tj2Rhn75YC1n9Q7Yjsxr1bcm")

tableName = 'Lottery'  #在这里写入表的名称
key = 'gameid'  #在这里写入修改字段的名称
value = 100  #在这里写入需要修改字段的值的名称

query = leancloud.Query(tableName)
#query.not_equal_to(key, value)   # 在这里可以配置更多的查询条件
query.limit(1000)

for item in query.find():
    TableName = leancloud.Object.extend(tableName)
    table = TableName.create_without_data(item.id) #实例
    table.set(key, 101)
    table.save()
    # price = item.get('price')
    # print(price)
    # if price <=300:
    #     table = TableName.create_without_data(item.id)
    #     table.set(key, 1)
    #     table.save()
    # elif price <=600:
    #     table = TableName.create_without_data(item.id)
    #     table.set(key, 2)
    #     table.save()
    # elif price <=900:
    #     table = TableName.create_without_data(item.id)
    #     table.set(key, 3)
    #     table.save()
    # elif price <=1300:
    #     table = TableName.create_without_data(item.id)
    #     table.set(key, 4)
    #     table.save()
    # else:
    #     table = TableName.create_without_data(item.id)
    #     table.set(key, 5)
    #     table.save()
