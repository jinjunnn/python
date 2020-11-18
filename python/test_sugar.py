import csv
import leancloud
from datetime import datetime
import json
import requests
from leancloud import cloudfunc
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# import common_redis

# 这个是电商项目
leancloud.init("XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

# 这段代码是将json list 转为object
# def upload_json_to_redis(url):
#     with open(url, 'r+', 1, 'UTF-8') as fr:
#         content = fr.read()
#         lst = content.split('\n')
#         for item in lst:
#             try:
#                 obj = json.loads(item)
#                 if 'sku' in obj.keys():
#                     print(obj['id'], json.dumps(obj['sku']))
#                     item_list = cloudfunc.run(
#                         'setField',
#                         key='item_' + obj['id'],
#                         field='sku',
#                         value=json.dumps(obj['sku']))
#             except:
#                 print('出错')
# upload_json_to_redis('/Users/mac/spader/download/123.json')

# 这段代码是下载所有商品数据
# def download_goods():
#     with open('/Users/mac/spader/resource/datas.json', 'w+', 1, 'UTF-8') as fr:
#         item_list = cloudfunc.run('keys',key='gid*')
#         for item in item_list:
#             print(item)
#             try:
#                 good = cloudfunc.run('getHash', key=item)
#                 fr.write(json.dumps(good))
#                 fr.write('\r')
#             except:
#                 pass

# 这段代码是批量 修改redis中的数据
# def modify_field():
#     item_list = cloudfunc.run('keys', key='item_*')
#     for item in item_list:
#         try:
#             goods = cloudfunc.run('getHash', key=item)
#             if 'pid' in goods.keys():
#                 _id = cloudfunc.run('setField', key=item,field='id',value=goods['pid'])
#                 print(_id)
#         except:
#             print('失败')

# modify_field()

# download_goods()

# 这段代码是翻译的代码
# from googletrans import Translator
# translator = Translator(service_urls=['translate.google.cn'])
# source = 'クレンジング'
# text = translator.translate(source, src='ja', dest='zh-cn').text
# print(text)

# 这段代码是将 csv数据转为json数据
# def trans_csv_to_json(url,result):
#     f1 = open(url, 'r')
#     fr = open(result, 'a+')
#     csv_file = csv.reader(f1)
#     for item in csv_file:
#         goods = {}
#         goods['brandid'] = item[0]
#         goods['brand'] = item[1]
#         goods['name'] = item[2]
#         goods['size'] = item[3]
#         goods['id'] = item[4]
#         goods['price'] = item[5]
#         goods['resource'] = item[6]
#         goods['image'] = item[7]
#         goods['images'] = json.loads(item[8])
#         goods['hot'] = item[9]

#         goods['sku'] = eval(item[10])

#         goods['content'] = item[11]
#         fr.write(json.dumps(goods))
#         fr.write('\r')

# trans_csv_to_json('/Users/mac/spader/download/sephora.csv',
#                   '/Users/mac/spader/download/sephora.json')

# result = cloudfunc.run('del_key', key='records*')

# result = cloudfunc.run('del_key', key='records*')


# result = cloudfunc.run('card',func='card',type='type',brand='brand',amount='amount',price='price',time='time',uid='uid',title='title',msg='msg')
# print(result)


# 这段代码将goods下载
# Todo = leancloud.Object.extend('Goods')
# result = cloudfunc.run('keys', key='item_*')
# print(len(result))
# for item in result:
#     try:
#         goods = Todo()
#         good = cloudfunc.run('getHash', key=item)
#         for k,v in good.items():
#             goods.set(k,v)
#         try:
#             goods.save()
#             time.sleep(0.002)
#             print(item)
#         except:
#             print(0)
#     except expression as identifier:
#         pass


# price = [
#     79, 88, 89, 93, 99, 103, 106, 110, 120, 122, 125, 130, 135, 147, 159, 170,
#     170, 178, 189, 223, 240, 246, 267, 396, 447, 525, 645, 654, 775
# ]

# # price.sort()
# # print(price)
# for item in price:
#     result = item * 6.3 + 130
#     print(item,'\t',result)

# 批量设置商品价格
# result = cloudfunc.run('get_list_details_new', key='shop_sugar_total_sell_list',begin=0,end=137)

# for item in result:
#     print(item['key'], item['price'], int(item['price']) + 60)
#     r = cloudfunc.run('setField', key=item['key'], field='price', value=int(item['price'])+60)
