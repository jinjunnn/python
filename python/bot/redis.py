#这个代码是用来进行redis操作的

import csv
import leancloud
from datetime import datetime
import json
import requests
from leancloud import cloudfunc

# 这个是电商项目
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


#   这段代码是进行redis数组的操作
def push_list():
    key = 'list_skincare_0001'
    lst = [
        '92005242', '92005452', '92004048', '92008254', '92004489', '92000001',
        '92000146', '92000619', '92000118', '92000120', '92000943', '92005813',
        '92001777', '92001780', '92006574', '92002356', '92002357', '92002359',
        '92003729', '92001757', '92001758', '92001759', '92001760', '92001761',
        '92001762', '92001763', '92001764', '92001765', '92004819', '92004820',
        '92008288', '92002026', '92002083', '92002341', '92004729', '92001827',
        '92001827', '92001827', '92003144', '92003145', '92003146', '92003147',
        '92006574', '92006574', '92001058', '92001059', '92001060', '92004123',
        '92006575', '92006576', '92006577', '92000005'
    ]
    for item in lst:
        i = 'item_'+item
        result = cloudfunc.run(
            'lpush', key=key, value=i)
        print(result)
# push_list()


#   给redis中的list去重
def upload_list(key, l):
    del_list = cloudfunc.run('del_key', key=key)
    for item in l:
        load = cloudfunc.run('rpush', key=key,value=item)
        print(key,item)

#   去重
def quchong_list():
    key = 'list_skin*'
    list_wrap = cloudfunc.run('keys', key=key)
    for i in list_wrap:
        result = cloudfunc.run('get_list_item', key=i, begin=0, end=-1)
        news_li = []
        for item in result:
            if item not in news_li:
                news_li.append(item)
        upload_list(i, news_li)

quchong_list()
