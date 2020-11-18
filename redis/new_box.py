#创建一个新的盲盒



import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


new_id = cloudfunc.run('getField',key='settings',field='act_id')
print(new_id)
new_key = 'act_'+new_id
new_link = '/pages/act/box/box?key='+new_key
act = {}
act['type'] =  ''                       	#
act['a_image'] = ''						#
act['b_image'] = ''
act['c_image'] = ''
act['d_image'] = ''
act['e_image'] = ''
act['f_image'] = ''
act['g_image'] = ''
act['h_image'] = ''
act['i_image'] = ''
act['j_image'] = ''
act['k_image'] = ''
act['l_image'] = ''
act['currency'] = 'wish'
act['price'] = ''
act['banner'] = ''
act['icon'] = 'http://lc-XBtceMXX.cn-n1.lcfile.com/e08a710e8f3fc249e647/%E7%9F%A9%E5%BD%A2.png'
act['title'] = ''
act['content'] = ''
act['detail'] = ''
act['id'] = new_id
act['key'] = new_key
act['link'] = new_link
act['image'] = ''
act['buttons'] = '立即参与'
act['share_card'] = ''
act['a'] = ''
act['b'] = ''
act['c'] = ''
act['d'] = ''
act['e'] = ''
act['f'] = ''
act['g'] = ''
act['h'] = ''
act['i'] = ''
act['j'] = ''
act['k'] = ''
act['l'] = ''
act['m'] = ''
result = cloudfunc.run('upload_actinfo_redis_backend', act=act)
print(result)
nextactid = cloudfunc.run('increField',key='settings',field='act_id',value=1)
print(nextactid)