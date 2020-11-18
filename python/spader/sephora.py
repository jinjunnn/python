import requests
from bs4 import BeautifulSoup
import lxml
import html5lib
import ssl
from selenium import webdriver
import json
import time
import csv
import re
from googletrans import Translator

item_url = 'https://m.sephora.com/api/users/profiles/current/product/P456430?skipAddToRecentlyViewed=false&preferedSku=2313534'
list_url = 'https://m.sephora.com/api/catalog/brands/1254?currentPage=1&pageSize=10&content=true&includeRegionsMap=true'
item_detail_url = 'https://m.sephora.com/product/yves-saint-laurent-rouge-volupte-rock-n-shine-lipstick-P454359?icid2=products%20grid:p454359'
start_url = 'https://m.sephora.com/brands-list'

proxies = {
    'https': 'https://127.0.0.1:1087',
    'http': 'http://127.0.0.1:1087'
}

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

f = open('/Users/mac/spader/resource/sephora.txt', 'w', 1, 'UTF-8')


def run_api_list_query():
    l = ['6014','6175','5945','6089','1073','5337','1254','6201','1517','1132','5869','3976','1741','1133','1070','1065','5644','2082','6218','6135','2084','1070']
    for item in l:
        url = 'https://m.sephora.com/api/catalog/brands/' + item + '?currentPage=1&pageSize=120&content=true&includeRegionsMap=true'
        api_list_query(item,url)
        time.sleep(5)

def run_api_item_query():
    f1 = open('/Users/mac/spader/resource/sephora_items.csv', 'r')
    csv_file = csv.reader(f1)
    for item in csv_file:
        url = 'https://m.sephora.com' + item[3]
        print(item[0],url)
        get_item_html_text(item[1],url)
        time.sleep(5)


def api_list_query(brandid,url):
    f1 = open('/Users/mac/spader/resource/sephora_items.csv', 'a+', 1, 'UTF-8')
    writer1 = csv.writer(f1)  #创建写的对象
    r = requests.get(url, proxies=proxies, headers=headers, timeout=90)
    goods = json.loads(r.text)
    products = goods['products']
    for product in products:
        writer1.writerow([brandid,product['productId'], product['targetUrl']])


def api_item_query(url):
    r = requests.get(url, proxies=proxies, headers=headers, timeout=90)
    goods = json.loads(r.text)
    f.write(str(goods))
    print('完成')
    # for product in products:
    #     print(product['productId'], product['targetUrl'])


def api_translate(source):
    translator = Translator(service_urls=['translate.google.cn'])
    text = translator.translate(source, src='en', dest='zh-cn').text
    return text



#请求详情页面
def get_item_html_text(brandid,url):
    r = requests.get(url, proxies=proxies, headers=headers, timeout=90)
    goods = {}
    soup = BeautifulSoup(r.text, 'lxml')
    soup.prettify()
    f.write(str(soup.prettify()))
    html = soup.find('div', class_='css-fxvh6r ')
    try:
        image = html.find('img').get('src')
    except:
        print('这个商品销售空了')
        return
    #删除 问号后的字符串
    goods['image'] = 'https://www.sephora.com' + image.split("?", 1)[0] + '?imwidth=450'
    images_wrap = html.find_all('img')
    images = []
    for item in images_wrap:
        try:
            i = item.get('data-llimg')
            i = 'https://www.sephora.com' + i.split("?", 1)[0] + '?imwidth=450'
            images.append(i)
        except:
            pass
    goods['images'] = json.dumps(images)
    print(image)
    try:
        goods['hot'] = html.find('span', class_='css-1leudl5 ').get_text()
    except:
        pass

    size = html.find('div', class_='css-1ezikxe ').get_text()
    goods['size'] = size.split("ITEM", 1)[0]
    goods['preferid'] = size.split("ITEM", 1)[1]
    goods['price'] = html.find('div', class_='css-slwsq8 ').get_text().replace('$','')
    goods['source'] = '美国丝芙兰专柜'
    goods['brand'] = html.find('span',class_="css-euydo4").get_text()
    goods['name'] = html.find('span',class_='css-0').get_text()
    sku = []
    sku_wrap = soup.find_all('img', class_='css-1p28rvx ')
    for item in sku_wrap:
        attr = {}
        attr['name'] = item.get('alt')
        if html.find('div', class_='css-slwsq8 ').get_text().replace('$', ''):
            attr['price'] = html.find(
                'div', class_='css-slwsq8 ').get_text().replace('$', '')
        if 'https://www.sephora.com' + item.get('src'):
            attr['image'] = 'https://www.sephora.com' + item.get('src')
        if html.find('div', class_='css-1ezikxe ').get_text():
            attr['id'] = html.find('div', class_='css-1ezikxe ').get_text()[-8:]
        sku.append(attr)
    goods['sku'] = json.dumps(sku)
    goods['brandid'] = brandid
    goods['content'] = soup.find('div', 'css-yc3z0f ').get_text()

    print_item(goods)


def print_item(goods):
    f_item = open('/Users/mac/spader/download/sephora.csv', 'a+')
    writer_item = csv.writer(f_item)  #创建写的对象
    good = []
    good.append(goods.get('brandid', ''))
    good.append(goods.get('brand', ''))
    good.append(goods.get('name', ''))
    good.append(goods.get('size', ''))
    good.append(goods.get('preferid', ''))
    good.append(goods.get('price', ''))
    good.append(goods.get('source', ''))
    good.append(goods.get('image', ''))
    good.append(goods.get('images', ''))
    good.append(goods.get('hot', ''))
    good.append(goods.get('sku', ''))
    good.append(goods.get('content', ''))
    # print(good)
    writer_item.writerow(good)
    f_item.close()


#   第一步：获取   brand_list
def get_brand_list(url):
    r = requests.get(url, proxies=proxies, headers=headers, timeout=90)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(str(soup.prettify()))
    f.write(str(soup.prettify()))
    # the_list = soup.find_all('a', 'css-1xey2kr ')
    # for items in the_list:
    #     urls = 'https://m.sephora.com' + items.get('href')
    #     # print(items)
    #     get_brand_id(urls)

    #     time.sleep(90)


run_api_item_query()