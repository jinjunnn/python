#``这个代码是将海带丝的数据上传到redis中。



# # coding: utf8
# import csv
# import requests
# import leancloud
# from leancloud import cloudfunc
# from io import StringIO
# leancloud.init(
#     "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

# f = open('/Users/mac/spader/resource/jp.csv', 'r')
# csv_file = csv.reader(f)
# i = 91005000
# for item in csv_file:
#     i = i + 1

#     name = cloudfunc.run('setField', key='item_' + str(i), field='name',value=item[1])
#     key = cloudfunc.run('setField', key='item_' + str(i), field='key', value='item_' + str(i))
#     price = cloudfunc.run('setField', key='item_' + str(i), field='content', value=item[3])
#     rpush = cloudfunc.run('rpush', key='list_jp_100', value='item_' + str(i))
#     print(rpush)
#     print(name,key,price,rpush)




import csv
import requests
import leancloud
from leancloud import cloudfunc
from io import StringIO
leancloud.init(
    "0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")


def get_content(url):
    r = requests.get("http://app.haidais.cn/wap/goodsintro.aspx?id=" + url)
    return r.content.decode('utf-8')


def get_images(lst):
    l = []
    for item in lst:
        l.append('http://app.haidais.cn' + item)
    return l


def get_image(url, key):
    print('http://app.haidais.cn' + url,key)
    r = requests.get('http://app.haidais.cn' + url, stream=True)
    data = StringIO('LeanCloud')
    file = leancloud.File(key, r.content)
    try:
        file.save()
        print(file.url)
        return file.url
    except:
        pass


def get_goods(idx):
    f1 = open('/Users/mac/spader/resource/haidaisi.csv', 'a+')
    writer1 = csv.writer(f1)  #创建写的对象

    url = "http://app.haidais.cn/apiservice.asmx/goodslist?barcode=&brandid=&categoryid=&categoryid2=&keyword=&pageindex=" + str(idx) + "&pagesize=200&sort=&sort2="
    r = requests.get(url)
    result = r.json()
    lists = []
    for item in result['data']:
        try:
            brand = item.get('BrandName', '')
            classic = item.get('CategoryName1', '')
            sub_classic = item.get('CategoryName2', '')
            size = item.get('Weight', '')
            pid = item.get('BarCode', '')
            brandid = item.get('BrandID', '')
            price = item.get('Price2', '')
            images = get_images(item.get('PicList', ''))
            image = get_image(item['Pic'], item['ID'])
            name = item.get('Name', '')
            ID = item.get('ID', '')
            content = get_content(item['ID'])
            lists.append([
                brand, classic, sub_classic, size, pid, brandid, price, images,
                image, name, ID, content
            ])
        except:
            pass

    writer1.writerows(lists)


for item in range(23,200):

    get_goods(item)



