import requests
from bs4 import BeautifulSoup
import re
import lxml
import ssl
from selenium import webdriver
import time
import csv

strat_index = 2197
start_url = 'https://www.matsukiyo.co.jp/store/online/search?category=001'

proxies = {
    'https': 'https://127.0.0.1:1087',
    'http': 'http://127.0.0.1:1087'
}

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
# f1 = open('/Users/mac/spader/resource/matsukiyo_list.csv', 'a')
f2 = open('/Users/mac/spader/download/matsukiyo_xihu.csv', 'a')
# writer1 = csv.writer(f1)  #创建写的对象

writer2 = csv.writer(f2)  #创建写的对象
writer2.writerow(['大类ID','子类ID',"条形码",'一级标签', "二级标签", "名称", "价格", "税","详情", "图片"])  #写入列的名称


#请求主页
#目前这个方法只能有二级子目录没有一级目录
def get_html_text(url):
    r = requests.get(url, headers=headers, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    soup.prettify()
    results = soup.find_all('a',class_='drilldown')
    for item in results:
        cateloryid = item.get('data-paramvalue')
        sub_classic = item.get_text().replace(" ","").replace('\n', '').replace('\r', '').replace('\t', '')
        if cateloryid:
            catelory_url = 'https://www.matsukiyo.co.jp/store/online/search?category='+ cateloryid
            print(catelory_url, sub_classic)
            #写入列的名称
            writer1.writerow([cateloryid,sub_classic,catelory_url])
        else:
            pass


#从商品列表页获取商品部分信息
def get_list_html_text(url,cid,sid,classic,sub_classic):
    r = requests.get(url, headers=headers, timeout=150)
    time.sleep(5)
    soup = BeautifulSoup(r.text, 'lxml')
    soup.prettify()
    try:
        results = soup.find("ul", id='itemList').find_all('li')
        for result in results:
            try:
                goods = {}
                goods['name'] = result.find('p', class_='ttl').get_text()
                price_wrap = result.find('p', class_='price').get_text().replace(',', '')
                price_list = re.findall(r'\d+', price_wrap)
                goods['price'] = price_list[0]
                tax_wrap = result.find('p', class_='price inTax').get_text()
                tax_list = re.findall(r'\d+', tax_wrap)
                goods['tax'] = tax_list[0]
                goods['sourceid'] = result.find('a', class_='favoriteHeart').get('data-code')
                goods['content'] = result.find('p', class_='rightBox').get_text()
                goods['image'] = 'https://www.matsukiyo.co.jp' + result.find('p', class_='img').find('a').find('img').get('src')
                goods['sub_classic'] = sub_classic
                goods['classic'] = classic
                goods['cid'] = cid
                goods['sid'] = sid
                redis_goods(goods)
            except:
                print('pass')
    except:
        print('列表页仿佛不对')


#请求详情页面
def get_item_html_text(url):
    pass

# 将数据上传到redis中
def redis_goods(goods):
    print(goods)
    good = []
    good.append(goods.get('cid', ''))
    good.append(goods.get('sid', ''))
    good.append(goods.get('sourceid', ''))
    good.append(goods.get('classic', ''))
    good.append(goods.get('sub_classic', ''))
    good.append(goods.get('name', ''))
    good.append(goods.get('price', ''))
    good.append(goods.get('tax', ''))
    good.append(goods.get('content', ''))
    good.append(goods.get('image', ''))
    print(good)
    writer2.writerow(good)


# 从resource 拿到列表页的列表，一一取出值，然后下载页面。
def get_csv_html_text():
    f = open('/Users/mac/spader/resource/matsukiyo_xihu.csv', 'r')
    csv_file = csv.reader(f)
    for item in csv_file:
        if int(item[0]) < strat_index:
            print('已经下载过')
            pass
        else:
            print(item[0],item[5], item[1], item[2], item[3], item[4])
            get_list_html_text(item[5],item[1],item[2],item[3],item[4])



get_csv_html_text()

# get_html_text(start_url)
