#   上传商品信息到redis
#   up_sephora()
#   up_matsukiyo()
import csv
import time
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

url = '/Users/mac/spader/resource/haidaisi.csv'
list_title_1 = 'list_sephora_'
list_title_2 = 'list_sephora_sub_'

# # SUGAR 项目
# leancloud.init(
#     "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

#  其他  项目
leancloud.init("0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")






def up_haidaisi(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)
    # del_list_key = cloudfunc.run('del_key', key=list_key)
    # del_sub_list_key = cloudfunc.run('del_key', key=sub_list_key)

    for item in csv_file:
        goods = {}
        list_key = list_title_1 + item[0]
        sub_list_key = list_title_2 + item[1]
        key = 'item_' + item[0]
        goods['key'] = key
        goods['pid'] = item[0]
        goods['brand'] = item[1]
        goods['name'] = item[5]
        goods['size'] = item[5]
        goods['content'] = item[12]
        goods['price'] = int(item[10]) + 15
        goods['fee'] = 6
        goods['tax'] = 0
        goods['image'] = item[13]
        goods['links'] = item[15]
        goods['images'] = json.dumps(item[14])
        source_object = {}
        source_object['id'] = item[4]
        source_object['shop'] = item[3]
        source_object['country'] = '日本'
        goods['source'] = json.dumps(source_object)
        print(item[0])
        for field, value in goods.items():
            try:
                set_item = cloudfunc.run(
                    'setField', key=key, field=field, value=value)
            except:
                pass

        try:
            push_sub_list = cloudfunc.run('lpush', key=list_key, value=key)
        except:
            pass

        # try:
        #     push_sub_sub_list = cloudfunc.run(
        #         'lpush', key=sub_list_key, value=key)
        # except:
        #     pass

# 上传丝芙兰商品execl 到redis中，并且加入到相对应的列队。
def up_sephora(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)
    for item in csv_file:
        key = 'item_' + item[4].strip()
        sku = json.dumps(eval(item[10]))
        content = item[11]

        # up_sku = cloudfunc.run('setField', key=key, field='sku', value=sku)
        # up_content = cloudfunc.run('setField', key=key, field='content', value=content)
        push_sub_sub_list = cloudfunc.run(
            'rpush', key='list_sephora_aaa', value=key)
        print(push_sub_sub_list)


def up_matsukiyo(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)
    # del_list_key = cloudfunc.run('del_key', key=list_key)
    # del_sub_list_key = cloudfunc.run('del_key', key=sub_list_key)

    for item in csv_file:
        goods = {}
        # list_key = list_title_1 + item[0]
        # sub_list_key = list_title_2 + item[1]
        key = 'item_' + item[2]
        goods['key'] = key
        goods['pid'] = item[2]
        goods['brand'] = item[4]
        goods['name'] = item[5]
        goods['size'] = item[5]
        goods['content'] = item[8]
        goods['price'] = item[6]
        goods['fee'] = 6
        goods['tax'] = 0
        goods['image'] = item[9]
        goods['images'] = json.dumps([])
        source_object = {}
        source_object['id'] = 1001
        source_object['shop'] = '松本清'
        source_object['country'] = '日本'
        goods['source'] = json.dumps(source_object)

        for field, value in goods.items():
            print(field, value)
            try:
                set_item = cloudfunc.run(
                    'setField', key=key, field=field, value=value)
            except:
                pass

        try:
            push_sub_list = cloudfunc.run('lpush', key=list_key, value=key)
        except:
            pass

        try:
            push_sub_sub_list = cloudfunc.run(
                'lpush', key=sub_list_key, value=key)
        except:
            pass


def push_item_to_list(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)

    for i in csv_file:
        # #   设置brand
        # try:
        #     if i[1]:
        #         print(i[1], 'item_' + i[0])
        #         result = cloudfunc.run('rpush', key=i[1], value='item_' + i[0])
        #         print(result)
        # except:
        #     pass
        #   设置版本
        try:
            print('item_' + i[0], i[8])
            result = cloudfunc.run('setField', key='item_' + i[0], field='edition', value='日本本土专柜版')
            print(result)
        except:
            pass
        # #   设置category
        # try:
        #     if i[8]:
        #         print('item_' + i[0], i[8])
        #         result = cloudfunc.run('setField', key='item_' + i[0], field='category', value=i[8])
        #         print(result)
        # except:
        #     pass

        # # #   设置weight
        # try:
        #     if i[10]:
        #         print('item_' + i[0], i[10])
        #         result = cloudfunc.run('setField', key='item_' + i[0], field='weight', value=i[10])
        #         print(result)
        # except:
        #     pass

        # # #   设置list
        # try:
        #     if i[7]:
        #         print('test_' + i[7], 'item_' + i[0])
        #         result = cloudfunc.run('rpush', key='test_'+i[7], value='item_'+i[0])
        #         print(result)
        # except:
        #     pass


def list_haidaisi(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)

    for item in csv_file:
        if item[7]:
            try:
                push_sub_list = cloudfunc.run('lpush', key=item[7], value='item_' + item[0])
                print(push_sub_list)
            except:
                pass
            finally:
                pass
        else:
            pass


def up_massage(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)
    # del_list_key = cloudfunc.run('del_key', key=list_key)
    # del_sub_list_key = cloudfunc.run('del_key', key=sub_list_key)

    for item in csv_file:
        goods = {}

        key = 'item_' + item[0]
        goods['key'] = key
        goods['id'] = item[0]
        goods['brand'] = item[3]
        goods['name'] = item[4]
        goods['size'] = item[4]
        goods['content'] = item[6]
        goods['price'] = item[5]
        goods['fee'] = 6
        goods['tax'] = 0
        goods['image'] = item[8]
        images = []
        if item[9]:
            images.append(item[9])
        goods['images'] = json.dumps(images)
        source_object = {}
        source_object['id'] = 1002
        source_object['shop'] = '丝芙兰'
        source_object['country'] = '美国'
        goods['source'] = json.dumps(source_object)

        # print(goods)
        # print(item[2],key)
        # for field, value in goods.items():
        #     print(field, value)
        #     try:
        #         set_item = cloudfunc.run(
        #             'setField', key=key, field=field, value=value)
        #     except:
        #         pass
        if item[2]:
            try:
                push_sub_list = cloudfunc.run('rpush', key=item[2], value=key)
                print(push_sub_list)
            except:
                pass




#   一个list 存的都是key  删除这个list里所有的key
def del_list_item_key(lst):
    r1 = cloudfunc.run('query_list', key=lst, begin=0, end=-1)
    print(r1)
    for item in r1:
        print(item)
        r2 = cloudfunc.run('del_one_key', key=item)
    r3 = cloudfunc.run('del_one_key', key=lst)





# del_list_item_key('list_wish_lottery')
# up_massage('/Users/mac/spader/download/0330/12345.csv')
# up_sephora('/Users/mac/spader/download/sephora.csv')
# list_haidaisi(url)
# push_item_to_list('/Users/mac/spader/resource/beauty.csv')
# up_haidaisi(url)

# r1 = cloudfunc.run('del_key', key='list_s*')
# r1 = cloudfunc.run('del_key', key='list_sephora_sub_top100')
# r1 = cloudfunc.run('del_key', key='list_dr*')
# msg_to_json()