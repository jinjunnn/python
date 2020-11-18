#上传 list


import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

f = open('/Users/mac/spader/upload/list_0108.csv', 'r')
csv_file = csv.reader(f)
for item in csv_file:
    # print(item)
    goods = {}
    goods['list_id'] = item[0]
    goods['shop_desc'] = item[1]
    goods['shop_name'] = item[2]
    goods['shop_images'] = item[3]

    result = cloudfunc.run('up_load_list_to_redis_from_execl', datas=goods)
    print('完成')