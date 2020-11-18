
import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

#  这个是电商
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

# good_csv = []
# goods_list = cloudfunc.run('getListItemHash', key='act*')
# for goods in goods_list:
#     print(
#         goods.get('title', ''), 
#         goods.get('content', ''), 
#         goods.get('image', ''))




#   这个是针对GOODS表
query = leancloud.Query('Trial')


for item in query.find():
    print(
    item.get('name', ''), 
    item.get('sub_name', ''), 
    item.get('images', '')[0])