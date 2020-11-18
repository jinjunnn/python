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

leancloud.init("XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

'''
目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格
理解： 淘宝的搜索接口 翻页的处理
技术路线：requests‐bs4‐re

功能：
1.导入详情页的id，放入list中
2.写好list_key
3.运行程序，将id数据上传到redis中，并加入到list_key中。

4.list_key 清单


onroad_goods_list_01    在途    美妆产品
onroad_goods_list_02    在途    轻奢
onroad_goods_list_03    在途    潮牌
onroad_goods_list_04    在途    电子产品

spot_goods_list_01      现货    美妆
spot_goods_list_02      现货    轻奢
spot_goods_list_03      现货    潮牌
spot_goods_list_04      现货    电子产品

futures_goods_list_01   期货    美妆
futures_goods_list_02   期货    轻奢
futures_goods_list_03   期货    潮牌
futures_goods_list_04   期货    电子产品

'''

#配置信息
#list列表
start_url = ''

#items 列表
items = ['5120258', '2921990', '5199459']

#将输入放在哪个 list中。
list_key = 'onroad_goods_list_02'

# 2：在途   3：预约期货     4：现货
classic = '02'

# 1:美妆    2：轻奢     3：潮牌     4 :电子产品
sub_classic = '02'


#步骤1：提交商品搜索请求，循环获取页面
def get_html_text(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    }
    try:
        coo = 't=85db5e7cb0133f23f29f98c7d6955615; cna=3uklFEhvXUoCAd9H6ovaVLTG; isg=BM3NGT0Oqmp6Mg4qfcGPnvDY3-pNqzF2joji8w9SGWTYBu241_taTS6UdFrF3Rk0; miid=983575671563913813; thw=cn; um=535523100CBE37C36EEFF761CFAC96BC4CD04CD48E6631C3112393F438E181DF6B34171FDA66B2C2CD43AD3E795C914C34A100CE538767508DAD6914FD9E61CE; _cc_=W5iHLLyFfA%3D%3D; tg=0; enc=oRI1V9aX5p%2BnPbULesXvnR%2BUwIh9CHIuErw0qljnmbKe0Ecu1Gxwa4C4%2FzONeGVH9StU4Isw64KTx9EHQEhI2g%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_0; hibext_instdsigdipv2=1; JSESSIONID=EC33B48CDDBA7F11577AA9FEB44F0DF3'
        cookies = {}
        for line in coo.split(';'):  # 浏览器伪装
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        r = requests.get(url, cookies=cookies, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'lxml')
        item_wrap = soup.select('.goods')  #通过类名进行查找带点，通过标签名查找不带点
        for item in item_wrap:
            title = item.find("a", class_="title").get('title')
            image = 'https:' + item.find(
                "img", class_="imgtag img-lazyload").get("data-src")[:-39]
            price = item.find("p", class_="price").find("span").get_text()[1:]
            detail_url = 'https:' + item.find(
                "div", class_="goodswrap promotion").find("a").get("href")
            nation = item.find(
                "span", class_="proPlace ellipsis").get_text()  #产地

            comments = item.find("a", class_="comments").get_text()
            content = get_item_html_text(detail_url)
            good = [
                '', '', title, price, image, content, comments, detail_url,
                nation, detail_url
            ]
            print(good)
            items.append(good)
        print(items)
        f = open('/Users/mac/spader/commodity/kaola.csv', 'a')
        print('已经打开文件')
        writer = csv.writer(f)
        print('开启csv')
        writer.writerow([
            '面膜眼膜', '品牌', '品名', '价格', '图片', '产品详情', '评论数量', '商品链接', '商城', '链接'
        ])
        print('写完第一条数据')
        writer.writerows(items)
        print('写完所有数据')
        f.close()

    except:
        return ''


#请求详情页面
def get_item_html_text(url):
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
        image = 'https:' + image_a.split('?')[0] + '?imageView&thumbnail=400x400'
        brand = soup.find('a', class_='brand').get_text()
        title = soup.find('dt', class_='product-title').get_text()
        content = soup.find('dt', class_='subTit').get_text()
        # size 没有开发好
        size = soup.find('div', class_='proValue').get_text()
        print(size.replace(" ", ""))
        # 构建对象
        goods = {}
        sells_key = 'sell_' + str(int(time.time()*1000))
        goods['key'] = sells_key
        goods['list_id'] = list_key
        goods['owner'] = 10000424
        goods['title'] = title
        goods['classic'] = classic
        goods['sub_classic'] = sub_classic
        goods['size'] = size.replace(" ", "")
        goods['content'] = content
        goods['price'] = 1000
        goods['fee'] = 0
        goods['etb'] = ''
        goods['eta'] = ''
        goods['image'] = image
        images = []
        goods['images'] = json.dumps(images)
        print(goods)
        for key, value in goods.items():
            redis_items(sells_key, key, value)
        list_items(list_key, sells_key)
    except:
        print('错误')
        return ''

# 步骤3：将数据上传到redis中。
def redis_items(key,field,value):
    result = cloudfunc.run('setField', key=key, field=field, value=value)
    print(result)

# 步骤4：将商品数据 放置到 商品列表中。
def list_items(wrap, key):
    result = cloudfunc.run('lpush', key=wrap, value=key)
    print(result)


def query_list():
    html = get_item_html_text(start_url)


def query_items():
    for item in items:
        item_page = 'https://goods.kaola.com/product/'+ item + '.html'
        print(item_page)
        get_item_html_text(item_page)
        time.sleep(1)

query_items()
