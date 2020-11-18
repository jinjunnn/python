import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc
# # SUGAR 项目
# leancloud.init(
#     "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


#  其他  项目
leancloud.init(
    "0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")

# get_field = cloudfunc.run('getField',key='settings',field='act_id')
# print(get_field)

# get_hash = cloudfunc.run('getHash',key='act_1011')
# print(get_hash)

#查询所有元素
# ge = cloudfunc.run('keys', key='gm_act*')
# for item in ge:
#     print(item)
#     ge = cloudfunc.run('del_key', key=item)
#     print(ge)

# 将集合中所有元素的  wish_price * 2
# results = cloudfunc.run('get_set_item_hash', key='wishs')
# print(results)
# for item in results:
#     print(item['key'])
#     print(item['wish_price'])
#     value = int(item['wish_price']) *2
#     print(value)
# result = cloudfunc.run('setField',key=item['key'],field='wish_price',value=value)
# print(result)

# 查询所有用户
# ge = cloudfunc.run('keys', key='user_*')
# for item in ge:
#     user = cloudfunc.run('getHash', key=item)
#     print(
#         user.get('uid', ''), user.get('nickName', ''), user.get(
#             'f_balance', ''), user.get('image', ''))

# 查看所有act
# dels = cloudfunc.run('del_key', key='acts')
# ge = cloudfunc.run('keys', key='act_1*')
# for item in ge:
#     print(item)
#     user = cloudfunc.run('setSet', key='acts',value=item)
#     # user = cloudfunc.run('del_key', key=item)
#     print(user)

# ge = cloudfunc.run('get_set_item_hash', key='sharees_10009515')
# for item in ge:
#     print(
#         item.get('uid', ''), item.get('nickName', ''), item.get(
#             'f_balance', ''), item.get('image', ''))

# Todo = leancloud.Object.extend('Test')
# query = Todo.query
# todo = query.get('5e285477d4b56c008e75c084')
# name = todo.get('name')
# ge = cloudfunc.run(
#     'setField', key='settings', field='share_page_rule', value=name)
# print(ge)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()

# options.add_argument('--no-sandbox')  #解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1920x3000')  #指定浏览器分辨率
# options.add_argument('--disable-gpu')  #谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars')  #隐藏滚动条, 应对一些特殊页面
# options.add_argument('blink-settings=imagesEnabled=false')  #不加载图片, 提升速度
# options.add_argument('--headless')  #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

# driver = webdriver.Chrome(options=options)
# driver.get('https://www.baidu.com')
# print(driver.page_source)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# # 创建chrome浏览器驱动，无头模式
# chrome_options = Options()
# # chrome_options.add_argument('--headless')
# chrome_options.add_argument("--start-maximized");
# driver = webdriver.Chrome(chrome_options=chrome_options)

# # 加载界面
# driver.get("https://m.sephora.com/brand/clinique")
# time.sleep(3)

# # 获取页面初始高度
# js = "return action=document.body.scrollHeight"
# height = driver.execute_script(js)
# print(height)

# # 将滚动条调整至页面底部
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(5)

# #定义初始时间戳（秒）
# t1 = int(time.time())

# #定义循环标识，用于终止while循环
# status = True

# # 重试次数
# num=0

# while status:
# 	# 获取当前时间戳（秒）
#     t2 = int(time.time())
#     # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
#     if t2-t1 < 30:
#         new_height = driver.execute_script(js)
#         if new_height > height :
#             time.sleep(1)
#             driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#             # 重置初始页面高度
#             height = new_height
#             # 重置初始时间戳，重新计时
#             t1 = int(time.time())
#     elif num < 3:                        # 当超过30秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待30秒
#         time.sleep(3)
#         num = num+1
#     else:    # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
#         print("滚动条已经处于页面最下方！")
#         status = False
#         # 滚动条调整至页面顶部
#         driver.execute_script('window.scrollTo(0, 0)')
#         break

# # 打印页面源码
# content = driver.page_source
# print(content)

# import requests
# from bs4 import BeautifulSoup
# import re
# import lxml
# import ssl
# from selenium import webdriver
# import time
# import csv

# start_url = 'https://www.matsukiyo.co.jp/store/online/search?category=005'

# proxies = {'https': 'https://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}

# headers = {
#     'user-agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }

# f1 = open('/Users/mac/spader/resource/matsukiyo_list.csv', 'a')
# writer1 = csv.writer(f1)  #创建写的对象

# #请求主页
# #目前这个方法只能有二级子目录没有一级目录
# def get_html_text(url):
#     r = requests.get(url, headers=headers, timeout=30)
#     soup = BeautifulSoup(r.text, 'lxml')
#     soup.prettify()
#     results = soup.find_all('a', class_='drilldown')
#     for item in results:
#         cateloryid = item.get('data-paramvalue')
#         sub_classic = item.get_text().replace(" ",
#                                               "").replace('\n', '').replace(
#                                                   '\r', '').replace('\t', '')
#         if cateloryid:
#             catelory_url = 'https://www.matsukiyo.co.jp/store/online/search?category=' + cateloryid
#             print(catelory_url, sub_classic)
#             #写入列的名称
#             writer1.writerow([cateloryid, sub_classic, catelory_url])
#         else:
#             pass

# get_html_text(start_url)

# # 这个功能是打印 松本清的一级目录
# import csv
# f = open('/Users/mac/spader/download/snacks_jp.csv', 'r')
# csv_file = csv.reader(f)
# lists = []
# for item in csv_file:
#     obj = {}
#     obj['name'] = item[3]
#     obj['key'] = 'list_snacks_jp_' + item[0]
#     if obj not in lists:
#         lists.append(obj)
#     print(lists)

# 这个功能是下载 维护热销产品清单的  JSON

# {
#     'name':
#     '保健养生 日本站',
#     'image':
#     'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
#     'top': [{
#             'name':'热门商品',
#             'image':'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
#             'key':'list_drug_jp_1112',
#         },{
#             'name':'丝芙兰热销榜单TOP100',
#             'image':'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
#             'key':'list_drug_jp_1112',
#         }],
#     'list': [{
#         'name': '汉方药',
#         'key': 'list_drug_jp_1112'
#     }, {
#         'name': '健康食品',
#         'key': 'list_drug_jp_1202'
#     }, {
#         'name': '减肥',
#         'key': 'list_drug_jp_1203'
#     }, {
#         'name': '滋养强壮',
#         'key': 'list_drug_jp_1107'
#     }, {
#         'name': '营养液',
#         'key': 'list_drug_jp_1108'
#     }, {
#         'name': '保健品',
#         'key': 'list_drug_jp_1200'
#     }, {
#         'name': '营养饮食',
#         'key': 'list_drug_jp_1201'
#     }, {
#         'name': '生发剂',
#         'key': 'list_drug_jp_1115'
#     }, {
#         'name': '生活改善',
#         'key': 'list_drug_jp_1120'
#     }, {
#         'name': '便秘药',
#         'key': 'list_drug_jp_1111'
#     }, {
#         'name': '肠胃药',
#         'key': 'list_drug_jp_1109'
#     }, {
#         'name': '湿疹皮炎',
#         'key': 'list_drug_jp_1113'
#     }, {
#         'name': '鼻炎治疗药',
#         'key': 'list_drug_jp_1104'
#     }, {
#         'name': '外用阵痛消炎',
#         'key': 'list_drug_jp_1118'
#     }, {
#         'name': '保健机能食品',
#         'key': 'list_drug_jp_1204'
#     }, {
#         'name': '整肠剂  止泻药',
#         'key': 'list_drug_jp_1110'
#     }, {
#         'name': '総合感冒薬',
#         'key': 'list_drug_jp_1102'
#     }, {
#         'name': '薬用酒',
#         'key': 'list_drug_jp_1122'
#     }, {
#         'name': '鎮痛解熱消炎剤',
#         'key': 'list_drug_jp_1101'
#     }, {
#         'name': '感冒辅助药',
#         'key': 'list_drug_jp_1105'
#     }, {
#         'name': '眼药',
#         'key': 'list_drug_jp_1100'
#     }, {
#         'name': '鎮咳去痰剤',
#         'key': 'list_drug_jp_1103'
#     }, {
#         'name': '口腔用剂',
#         'key': 'list_drug_jp_1115'
#     }]
# },
# {
#     'name':
#     '网红零食 日本站',
#     'image':
#     'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
#     'list': [{
#         'name': '半生菓子',
#         'key': 'list_snacks_jp_5507'
#     }, {
#         'name': '口香糖',
#         'key': 'list_snacks_jp_5500'
#     }, {
#         'name': '米菓',
#         'key': 'list_snacks_jp_5504'
#     }, {
#         'name': '巧克力饼干',
#         'key': 'list_snacks_jp_5502'
#     }, {
#         'name': '焼菓子',
#         'key': 'list_snacks_jp_5505'
#     }, {
#         'name': '嗜好品',
#         'key': 'list_snacks_jp_5509'
#     }, {
#         'name': '糖果',
#         'key': 'list_snacks_jp_5501'
#     }, {
#         'name': '甜点',
#         'key': 'list_snacks_jp_5511'
#     }, {
#         'name': '珍味',
#         'key': 'list_snacks_jp_5508'
#     }, {
#         'name': '子供菓子',
#         'key': 'list_snacks_jp_5506'
#     }]
# }

#   这个功能是将图片下载到一个地址
# coding: utf8
# import csv
# import requests
# import leancloud
# from leancloud import cloudfunc
# from io import StringIO
# leancloud.init(
#     "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

# def download_img(img_url, key,idx):
#     f1 = open('/Users/mac/spader/resource/miss_download_keys.csv', 'a')
#     writer1 = csv.writer(f1)  #创建写的对象
#     header = {
#         "Authorization":
#         "Bearer " + 'fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda'
#     }  # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
#     r = requests.get(img_url, headers=header, stream=True)
#     if r.status_code == 200:
#         open('/Users/mac/spader/images/' + key +'.jpg', 'wb').write(
#             r.content)  # 将内容写入图片
#         try:
#             data = StringIO('LeanCloud')
#             file = leancloud.File(key, r.content)
#             file.save()
#             # print(file)
#             try:
#                 print(file.url)
#                 image = cloudfunc.run('setField', key=key,field='image',value=file.url)
#                 print(idx,key,image)
#             except:
#                 print('redis错误,key=',key)
#                 pass
#         except:
#             writer1.writerow([idx, key])
#             print('misload',idx, key)
#     else:
#         writer1.writerow([idx,key])
#         print('misload,key=', idx, key)
#         pass
#     del r

# if __name__ == '__main__':
#     # 下载要的图片
#     f = open('/Users/mac/spader/resource/item_keys.csv', 'r')
#     csv_file = csv.reader(f)
#     for item in csv_file:
#         try:
#             image = cloudfunc.run('getField', key=item[1],field='image')
#             download_img(image,item[1],item[0])
#         except:
#             print('redis错误')
#             pass

#   这部分代码是把所有的数据下载到execl
# result = cloudfunc.run('keys', key='item*')
# lst = []
# for idx, item in enumerate(result):
#     print(idx,item)
#     lst.append([idx,item])
# print(lst)
# f1 = open('/Users/mac/spader/resource/item_keys.csv', 'a')
# writer1 = csv.writer(f1)  #创建写的对象
# writer1.writerows(lst)

# import csv
# f = open('/Users/mac/spader/resource/top100_jp.csv', 'r')
# csv_file = csv.reader(f)
# i = 91000000
# for item in csv_file:
#     i = i + 1
#     goods = {
#         'price':item[1],
#         'name':item[0]
#     }

#     name = cloudfunc.run('setField', key='item_' + str(i), field='name',value=item[0])
#     key = cloudfunc.run('setField', key='item_' + str(i), field='key', value='item_' + str(i))
#     price = cloudfunc.run('setField', key='item_' + str(i), field='price', value=item[1])
#     rpush = cloudfunc.run('rpush', key='list_beauty_makeup_jp_top100', value='item_' + str(i))
#     print(rpush)
#     # print(name,key,price,rpush)

# r1 = cloudfunc.run(
#     'del_key', key='hs_*')

#   list 去重
# li = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
# news_li = []
# for i in li:
#     if i not in news_li:
#         news_li.append(i)
# print(news_li)

# uid = 100002000
# for item in range(500):
#     uid = uid + 1
#     result = cloudfunc.run(
#         'update_handsel',
#         handsel_key='hs_100000008_1005',
#         uid=uid,
#         goodid='1005',
#         gid='1005',
#         is_new_user=True,
#         code='jgtQ',
#         key='records_*')

#     print(result)

# python 字符串占位符

# s = "{0}-{1},{2}".format("zhang", 2018, 2019)
# print(s)

# s = "{name},{year}-{net}".format(name="phil", year=2019, net="blog.csdn.net")
# print(s)

# s = "{name},{0}".format(2019, name="zhangphil")
# print(s)

# result = cloudfunc.run('get_list_details_new', key='list_handsel', begin=0, end=4)

# print(result)

# 这个是测试群抽奖的代码
# user = {}
# uid = 10000000

# for i in range(130):
#     uid = uid + 1
#     user['name'] = 'pharaon'
#     user['image'] = 'https://wx.qlogo.cn/mmopen/vi_32/CEWufvUZXsX1IB1fd0ejrh5pV4o2zQ88klAwdPwoZJydicUt2FLjZAT65JljgQLgHvMX68ib9KtC3YtHdZbXmKqQ/132'
#     user['get'] = False
#     user['uid'] = uid
#     value = json.dumps(user)
#     print(value)

#     cloudfunc.run(
#         'setSet',
#         key='gl_20200925_G56y35RzRhfQHt5FJ9EIbsBEBPGk_92004139',
#         value=value)

# result = cloudfunc.run(
#     'getSet',
#     key='gl_20200819_tG56y35XysCANYwJXngcJwWHDVgpE_92004139')

# for item in result:
#     print(json.loads(item))

# 这个是测试限定抽奖的代码
# result = cloudfunc.run('query_users_infors', users=['19960966', '10000585', '10000708'])
# print(result)

# result = cloudfunc.run(
#     'query_limit_lottory', uid='10001098', sid='10000000', gid='92004139',code='jgtQ')
# print(result)

# result = cloudfunc.run(
#     'limit_lottery', uid='10001098', sid='1000000', gid='92004139',code='jgtQ')
# print(result)

# f = open('/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/python/resource/sephora.csv','r')
# csv_file = csv.reader(f)
# for item in csv_file:
#     goods = 'item_'+item[0]
#     good = cloudfunc.run('getHash', key=goods)
#     if good:
#         print(good)
#         cloudfunc.run('setField', key='test_' + good['id'], field='title', value=good['name'])
#         cloudfunc.run('setField', key='test_' + good['id'], field='image', value=good['image'])
#         cloudfunc.run('setField', key='test_' + good['id'], field='time', value=good['id'])
#         cloudfunc.run('setField', key='test_' + good['id'], field='brand', value=good['brand'])
#         cloudfunc.run('setField', key='test_' + good['id'], field='content', value=good['content'])
#         cloudfunc.run('setField',key='test_' + good['id'],field='price',value=int(good['price']) - 10)
#         cloudfunc.run('setField', key='test_' + good['id'], field='status', value=1)
#         cloudfunc.run('lpush',key='shop_sugar_total_sell_list',value='test_' + good['id'])
#     else:
#         cloudfunc.run('del_key',key='item_'+item[0])
#         print('item_'+item[0],None)

# results = cloudfunc.run('keys', key='item_*')
# for result in results:
#     try:
#         goods = cloudfunc.run('getHash', key=result)
#         print(goods.get('brand'))
#         if goods.get('brand'):
#             r = cloudfunc.run('setSet', key='brands', value=goods.get('brand'))
#             print(r)
#     except:
#         pass

# r = cloudfunc.run('getSet', key='brands')
# print(r)

s = [
    "KIEHL'S/科颜氏", 'Freeplus/芙丽芳丝', 'Armani/阿曼尼/阿玛尼', 'Sloggi/黛安芬',
    'PANDORA/潘多拉', 'PDC/碧迪皙', 'LA MER/海蓝之谜', 'DECORTE/黛珂', 'Adidas/阿迪达斯',
    'Curel/珂润', 'Dior/迪奥', 'LAB SERIES/朗仕', 'BOBBI BROWN/芭比波朗', 'La Mer',
    'Nintendo/任天堂', 'DENTISTE', 'IPSA/茵芙纱', 'Shiseido/资生堂', 'Fancl/芳珂',
    'Apple/苹果', 'IQOS', 'POLA/宝丽', 'DECORTE/黛珂', 'La prairie/莱珀妮',
    'CLINIQUE/倩碧', 'TF/TOM FORD', 'Dior', 'NARS', '雅诗兰黛/Estee Lauder',
    'Guerlain/娇兰', 'HACCI', 'BIODERMA/贝德玛', 'POLA/宝丽', 'IPSA/茵芙莎', 'RMK',
    'SUQQU', 'LANCOME/兰蔻', "L'OREAL/欧莱雅", 'Givenchy/纪梵希', 'Elégance/雅莉格丝',
    'MAC/魅可', 'SISLEY/希思黎', 'Freeplus/芙丽芳丝', 'Dyson/戴森', 'Clarins/CLARINS/娇韵诗',
    'HABA/无添加主义', 'CHANEL/香奈儿', 'CPB/肌肤之钥', 'HR/赫莲娜', 'SKII/SK2', 'YSL/圣罗兰',
    'BIOTHERM/碧欧泉', 'NIKE/耐克', 'Versace/范思哲', "Kiehl's/科颜氏", 'HABA',
    'FANCL/芳珂', 'ReFa', 'GUERLAIN/娇兰',  'Tiffany&Co./蒂芙尼', '理肤泉',
    'GUCCI/古驰', 'Miu Miu'
]

result = []
for item in s:
    for i in item.split('/'):
        obj = {}
        obj['name'] = i
        obj['value'] = item
        result.append(obj)

print(result)

