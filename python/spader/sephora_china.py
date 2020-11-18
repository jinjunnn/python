import requests
import re
from bs4 import BeautifulSoup
import lxml
import csv
'''
目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格
理解： 淘宝的搜索接口 翻页的处理
技术路线：requests‐bs4‐re
'''

f = ('/Users/mac/spader/download/sephora_china.csv', 'a')
writer = csv.writer(f)  #创建写的对象

#步骤1：提取所有的列表页
def get_list(url):
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
        product_wrap = soup.find("div", class_="module-pagination-page").find_all('a')
        p = product_wrap.pop().get_text()
        for item in range(1,int(p)+1):
            ul = url[:-2] + str(item) + '/'
            lst = get_html_text(ul)
    except:
        return ''


#步骤2:提取列表页字段
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
        product_wrap = soup.find_all("div", class_="p_cont")
        items = []
        for item in product_wrap:
            image = item.find("img").get('src')
            brand = item.find('div', class_='p_brandEn').get_text()
            name = item.find('div', class_='p_productCN').get_text()
            price = item.find('div', class_='p_discount commonFontPrice').get_text()
            link = item.find('a', target='_blank').get('href')
            goods = [brand,name,price,image,link]
            items.append(goods)
        writer.writerows(items)
    except:
        return ''





def main():
    start_url = 'https://www.sephora.cn/brand/ysl-108/page1/'
    html = get_list(start_url)


main()
