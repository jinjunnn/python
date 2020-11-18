#  做一些快捷的redis操作

import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


# get_field = cloudfunc.run('getField',key='settings',field='act_id')
# print(get_field)


# get_hash = cloudfunc.run('getHash',key='act_1011')
# print(get_hash)

set_field = cloudfunc.run('setField',key='settings',field='act_id',value='1012')
print(set_field)