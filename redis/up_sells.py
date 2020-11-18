#上传某个列表的商品
#并将商品放在列表的集合中

import csv
import time
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

f = open('/Users/mac/spader/upload/01.csv', 'r')
csv_file = csv.reader(f)
# renew/create
for item in csv_file:
    # print(item)
    goods = {}

    if item[3]=='02':
        list_id = 'onroad_goods_list_'
    if item[3]=='03':
        list_id = 'futures_goods_list_'
    if item[3]=='04':
        list_id = 'spot_goods_list_'
    sells_key = 'sell_' + str(int(time.time()*1000))
    goods['key'] = sells_key
    goods['list_id'] = list_id + item[4]
    goods['owner'] = 10000424
    goods['title'] = item[1]
    goods['classic'] = item[3]
    goods['sub_classic'] = item[4]
    goods['size'] = item[5]
    goods['content'] = item[6]
    goods['price'] = item[7]
    goods['fee'] = item[8]
    goods['etb'] = item[9]
    goods['image'] = item[10]
    goods['images'] = json.dumps(item[11])


    for key, value in goods.items():
        print(key,value)
        result = cloudfunc.run('setField', key=sells_key, field=key, value=value)
    result2 = cloudfunc.run('lpush', key=goods['list_id'], value=sells_key)
    print(goods['list_id'], sells_key)
