#   将我的抽奖数据设置为即将抽奖成功

import csv
import leancloud
from datetime import datetime
import time
import json
from leancloud import cloudfunc
#  这个是电商
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


uid = '10001098'
expired = int(time.time() * 1000) +16783000
times = 127

def update_lottery_result():

    result = cloudfunc.run('get_list_item', key='list_handsel', begin=0, end=-1)
    for item in result:
        good = cloudfunc.run('getHash', key=item)

        key = "hs_{}_{}".format(uid, good['id'])
        total = '{}00'.format(good['price'])
        paid = int(total) - 47
        goodid = good['id']

        print(key,total,paid,goodid,uid,times)
        cloudfunc.run('setField', key=key, field='expired', value=expired)
        cloudfunc.run('setField', key=key, field='total', value=total)
        cloudfunc.run('setField', key=key, field='key', value=key)
        cloudfunc.run('setField', key=key, field='paid', value=paid)
        cloudfunc.run('setField', key=key, field='goodid', value=goodid)
        cloudfunc.run('setField', key=key, field='times', value=times)
        cloudfunc.run('setField', key=key, field='uid', value=uid)



update_lottery_result()