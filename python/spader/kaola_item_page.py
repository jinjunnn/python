# -- coding: utf-8 --
import sys
import time
import requests
import re
from bs4 import BeautifulSoup
import lxml
import csv
import json
import leancloud
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

items = ['5624893', '6127296']
f1 = open('/Users/mac/spader/resource/kaola0001.csv', 'a+')
writer1 = csv.writer(f1)  #创建写的对象

#请求详情页面
def get_item_html_text(url,item):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
    }
    results = {}
    try:
        coo = 't=85db5e7cb0133f23f29f98c7d6955615; cna=3uklFEhvXUoCAd9H6ovaVLTG; isg=BM3NGT0Oqmp6Mg4qfcGPnvDY3-pNqzF2joji8w9SGWTYBu241_taTS6UdFrF3Rk0; miid=983575671563913813; thw=cn; um=535523100CBE37C36EEFF761CFAC96BC4CD04CD48E6631C3112393F438E181DF6B34171FDA66B2C2CD43AD3E795C914C34A100CE538767508DAD6914FD9E61CE; _cc_=W5iHLLyFfA%3D%3D; tg=0; enc=oRI1V9aX5p%2BnPbULesXvnR%2BUwIh9CHIuErw0qljnmbKe0Ecu1Gxwa4C4%2FzONeGVH9StU4Isw64KTx9EHQEhI2g%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_0; hibext_instdsigdipv2=1; JSESSIONID=EC33B48CDDBA7F11577AA9FEB44F0DF3'
        cookies = {}
        for line in coo.split(';'):  # 浏览器伪装
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        r = requests.get(url, cookies=cookies, headers=headers, timeout=60)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, 'lxml')
        #获取数据
        image_a = soup.find("li", class_="active").find("img").get("src")
        image = 'https:' + image_a.split(
            '?')[0] + '?imageView&thumbnail=400x400'
        brand = soup.find('a', class_='brand').get_text()
        title = soup.find('dt', class_='product-title').get_text()
        content = soup.find('dt', class_='subTit').get_text()
        # size 没有开发好
        size = soup.find('div', class_='proValue').get_text()
        # 构建对象
        print(type(item))
        print(item[0])
        print(item[1])
        goods = [item[0],item[1],title,content,image]
        return goods
    except:
        print('错误')
        return []


# 步骤3：将数据上传到redis中。
def redis_items(key, field, value):
    result = cloudfunc.run('setField', key=key, field=field, value=value)
    print(result)


def query_items():
    lists = []
    f = open('/Users/mac/spader/resource/kaola0002.csv', 'r')
    csv_file = csv.reader(f)
    for item in csv_file:
        item_page = 'https://goods.kaola.com/product/' + item[0] + '.html'
        goods = get_item_html_text(item_page,item)
        print(goods)
        lists.append(goods)
        time.sleep(1)
    writer1.writerows(lists)

query_items()
