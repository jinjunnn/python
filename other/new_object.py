# 转移某个表的数据到另外的表
import leancloud
from datetime import datetime
import json

leancloud.init(
    "evYA8nbQwsUuU30S2UDt9UcI-gzGzoHsz", master_key="Tj2Rhn75YC1n9Q7Yjsxr1bcm")
# 这里配置需要添加的Lottery表的相关PROPERTY
query = leancloud.Query('Property')
query.limit(1000)
id = 1199

for item in query.find():
    Commodity = leancloud.Object.extend('Commodity')
    commodity = Commodity()
    commodity.set('role', item.get('role'))
    commodity.set('name', item.get('name'))
    commodity.set('summary', item.get('summary'))
    commodity.set('display', 1)
    commodity.set('price', item.get('price'))
    commodity.set('image', item.get('image'))
    commodity.set('prior', item.get('prior'))
    commodity.set('hot', True)
    commodity.set('id', id)
    commodity.set('rank', item.get('rank'))
    commodity.set('property', item.get('property'))
    commodity.set('supplier', item.get('supplier'))
    commodity.set('gameid', item.get('gameid'))
    commodity.save()
    id = id + 1
print(list)
