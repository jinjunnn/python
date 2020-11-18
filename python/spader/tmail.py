# 爬取 天猫商城   详情页的信息

import requests
import re
from bs4 import BeautifulSoup
import lxml
import csv
import time
'''
天猫爬虫
输入天猫商品 id 列表，将列表的数据上传到redis中。
'''

list = []
items = []


#请求详情页面
def get_item_html_text(url):
    print('进入详情页')
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
    }
    results = {}
    results['image'] = ''
    results['params'] = ''
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

        images_wrap = soup.find("img", id="J_ImgBooth").get('src')
        print(images_wrap)
        url = images_wrap[1].find("a").find("img")['src'][:-12]
        image = 'https:' + url + '430x430q90.jpg'

        params_wrap = soup.find("ul", id="J_AttrUL").find_all("li")
        params = []
        for item in params_wrap:
            params.append(item.get_text())
        results['image'] = image
        results['params'] = params
        return results

    except:
        return results


# 步骤2：对于每个页面，提取商品名称和价格信息
def parse_page(ilt, html):
    try:
        plt = re.findall(
            r'\"view_price\"\:\"[\d\.]*\"',
            html)  # findall搜索全部字符串，viex_price是源代码中表价格的值，后面的字符串为数字和点组成的字符串
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',
                         html)  # 找到该字符串和后面符合正则表达式的字符串
        for i in range(len(plt)):
            price = eval(plt[i].split(':')
                         [1])  # re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
            title = eval(
                tlt[i].split(':')[1])  # 将re获得的字符串以：为界限分为两个字符串,并取第二个字符串
            ilt.append([price, title])
    except:
        print('')


# 步骤3：将信息输出到屏幕上
def print_goods_list(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  # 长度为多少
    print(tplt.format('序号', '价格', '名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    item_page = 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.40.1be9bc1bT2FoQk&id=579791278840&skuId=3854157308697&user_id=1917047079&cat_id=2&is_b=1&rn=20d6894f2c4041b3e7119fb6c4466c59'
    get_item_html_text(item_page)


main()