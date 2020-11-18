#下载user


import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

good_csv = []
goods_list = cloudfunc.run('getListItemHash', key='user_*')
for goods in goods_list:
    good = []
    good.append(goods.get('uid', ''))
    good.append(goods.get('nickName', ''))
    good.append(goods.get('city', ''))
    good.append(goods.get('consume', ''))
    good.append(goods.get('f_balance', ''))
    good.append(goods.get('f_consume', ''))
    good.append(goods.get('gender', ''))
    good.append(goods.get('i_balance', ''))
    good.append(goods.get('i_consume', ''))
    good.append(goods.get('image', ''))
    good.append(goods.get('balance', ''))
    good.append(goods.get('commission', ''))
    good.append(goods.get('share_times', ''))
    good.append(goods.get('sharer', ''))
    good.append(goods.get('vip', ''))
    good.append(goods.get('watch_times', ''))
    good.append(goods.get('city', ''))
    good_csv.append(good)
    print(good)
# print(good_csv)
f = open('/Users/mac/spader/download/user_01010.csv', 'a')
writer = csv.writer(f)  #创建写的对象
writer.writerow([
    "uid", "nickName", "city", "consume", "f_balance", "f_consume", "gender",
    "i_balance", "i_consume", "image", "balance", "commission", "share_times",
    "sharer", "vip", "watch_times", "city"
])  #写入列的名称
writer.writerows(good_csv)
f.close()
