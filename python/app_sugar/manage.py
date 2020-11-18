# -- coding: utf-8 --
import sys
import time
import requests
import os
import re
from bs4 import BeautifulSoup
import lxml
import csv
import leancloud
from leancloud import cloudfunc
from datetime import datetime

# 这个是电商项目
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

#   更新活动页面
def update_team_act(title,image):
    with open('/Users/mac/spader/resource/team_text.txt', 'r+') as fr:
        content = fr.read()
        set_content = cloudfunc.run('setField', key='settings', field='teams_gift_content', value=content)
        set_image = cloudfunc.run('setField', key='settings', field='teams_gift_images', value=image)
        set_title = cloudfunc.run('setField', key='settings', field='teams_gift_title',value=title)
        print(set_content)
        print(set_image)
        print(set_title)

# update_team_act('雅诗兰黛小棕瓶拼手气红包，手气最佳免费赠送','http://lc-XBtceMXX.cn-n1.lcfile.com/1643f7223eca3ab7573f/WechatIMG2446.jpeg')