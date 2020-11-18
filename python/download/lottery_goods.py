# 管理商品的上传和下载

import csv
import leancloud
from datetime import datetime
import json
import requests
from leancloud import cloudfunc

# 这个是电商项目
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


# 下载redis 的 抽奖商品数据，并存储在csv 中
def download_goods(url,list_key):
    f = open(url, 'a+')
    writer = csv.writer(f)  #创建写的对象
    lists = []
    result = cloudfunc.run('get_list_details_new', key = list_key,begin=0,end=-1)
    for item in result:
        name = item.get('name')
        _id = item.get('id')
        price = item.get('price')
        image = item.get('image')
        key = item.get('key')
        ll_times = item.get('ll_times')
        limit_lottery_ended = item.get('limit_lottery_ended')
        gl_times = item.get('gl_times')
        group_lottery_ended = item.get('group_lottery_ended')
        lists.append([_id,name,image,'','',price,ll_times,limit_lottery_ended,gl_times,group_lottery_ended])
    writer.writerows(lists)


def load_goods(url, list_key):
    f = open(url, 'r')
    csv_file = csv.reader(f)

    for item in csv_file:
        i = item[0]
        key = 'item_' + item[0]
        cloudfunc.run('setField', key=key, field='id', value=item[0])
        cloudfunc.run('setField', key=key, field='key', value=key)
        cloudfunc.run('setField', key=key, field='name', value=item[1])
        cloudfunc.run('setField', key=key, field='image', value=item[2])
        cloudfunc.run('setField', key=key, field='price', value=item[5])
        cloudfunc.run('setField', key=key, field='ll_times', value=item[4])
        cloudfunc.run('setField', key=key, field='limit_lottery_ended', value=item[5])
        cloudfunc.run('setField', key=key, field='gl_times', value=item[6])
        cloudfunc.run('setField', key=key, field='limit_lottery_ended', value=item[7])
        cloudfunc.run('setField', key=key, field='gl_times', value=item[8])
        cloudfunc.run('setField', key=key, field='group_lottery_ended', value=item[9])
        cloudfunc.run('setField', key=key, field='link', value=item[10])
        push_sub_sub_list = cloudfunc.run('rpush', key='list_handsel', value=key)


load_goods('/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/python/lottery_list.csv',
    'list_handsel')

# download_goods('/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/python/lottery_list.csv','list_handsel')
