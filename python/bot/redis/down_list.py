import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

good_csv = []
goods_list = cloudfunc.run('getListItemHash', key='list*')
for goods in goods_list:
    good = []
    good.append(goods.get('list_id', ''))
    good.append(goods.get('shop_desc', ''))
    good.append(goods.get('shop_name', ''))
    good.append(goods.get('shop_images', ''))
    good_csv.append(good)
    print(good)
# print(good_csv)
f = open('/Users/mac/spader/goods/list_0108.csv', 'a')
writer = csv.writer(f)  #创建写的对象
writer.writerow([
    "list_id", "shop_desc", "shop_name", "shop_images"
])  #写入列的名称
writer.writerows(good_csv)
f.close()
