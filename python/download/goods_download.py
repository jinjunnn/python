import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc
# # SUGAR 项目
# leancloud.init(
#     "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

#  其他  项目
leancloud.init(
    "0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")

'''

将redis数据下载到leancloud


'''
goods = cloudfunc.run('keys', key='item_*')

for key in goods:
    Goods = leancloud.Object.extend('Goods')
    g = Goods()
    try:
        print(key)
        good = cloudfunc.run('getHash', key=key)
        for k, v in good.items():
            g.set(k, v)
        try:
            g.save()
            print('上传{}成功'.format(key))
        except print(1):
            pass
    except:
        print(0)
        pass