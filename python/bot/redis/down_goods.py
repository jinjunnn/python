import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

good_csv = []
goods_list = cloudfunc.run('getListItemHash', key='gid_*')
for goods in goods_list:
    good = []
    good.append(goods.get('id', ''))
    good.append(goods.get('name', ''))
    good.append(goods.get('tags', ''))
    good.append(goods.get('sub_name', ''))
    good.append(goods.get('prior', ''))
    good.append(goods.get('price', ''))
    good.append(goods.get('content', ''))
    good.append(goods.get('images', ''))
    good.append(goods.get('share_discount', ''))
    good.append(goods.get('fee', ''))
    good.append(goods.get('trans_fee', ''))
    good.append(goods.get('commission', ''))
    good.append(goods.get('reason', ''))
    good.append(goods.get('remark', ''))
    good.append(goods.get('details', ''))
    good.append(goods.get('infors', ''))
    good.append(goods.get('list_id', ''))
    good_csv.append(good)
    print(good)
print(good_csv)
f = open('/Users/mac/spader/goods/0108.csv', 'w')
writer = csv.writer(f)  #创建写的对象
writer.writerow([
    "id", "品牌", "标签", "品名", "优先级", "价格", "商品详情","商品主图", "分享奖励", "手续费", "运费", "佣金","购买原因","备注", "详情图片", "参数图片", "list_id"
])  #写入列的名称
writer.writerows(good_csv)
f.close()

















# goods = {}

# result = cloudfunc.run('up_load_good_to_redis_from_execl', datas=goods)
# print('完成')
