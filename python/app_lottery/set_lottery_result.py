#   设置抽奖结果

import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc
#  这个是电商
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


'''



这段代码是将每日的抽奖数据上传


'''




times = 20133
codes = '07701'

lotterys = 518969
lotterys_first_get = 6
lotterys_second_get = 481

def update_lottery_result():
    #   1.设置当期中奖的数据
    lottery_result = cloudfunc.run('setField', key='lottery_result', field=str(times),value=codes)
    #   2.settings 里设置 period
    period = cloudfunc.run('setField', key='settings', field='period',value=times+1)
    #   3.lottery_app_settings  的 first_reward
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='first_reward',value=lotterys_first_get)
    #   4.lottery_app_settings  的 second_reward
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='second_reward',value=lotterys_second_get)
    #   5.lottery_app_settings  的 lotterys
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='lottery_times',value=lotterys)
    #   6.lottery_app_settings  的 period
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='period',value=times+1)
    #   7.lottery_app_settings  的 pre_code
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='pre_code',value=codes)
    #   8.lottery_app_settings  的 pre_period
    first_reward = cloudfunc.run('setField', key='lottery_app_settings', field='pre_period',value=times)

update_lottery_result()