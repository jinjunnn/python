import csv
import time
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

#  其他  项目
leancloud.init(
    "0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")


'''

这段代码是将execl的商品数据数据上传到redis中

'''

url = '/Users/mac/Library/Mobile Documents/com~apple~Numbers/Documents/resource/list_wish_lottery.csv'


def load_lottery_item(url):
    f = open(url, 'r')
    csv_file = csv.reader(f)
    for item in csv_file:
        i = item[0]
        key = 'item_' + str(i)
        # print(key)
        seller = msg_to_json(item[6], item[7], item[8], item[9], item[10],
                             item[11], item[12])

        cloudfunc.run('setField', key=key, field='id', value=i)
        cloudfunc.run('setField', key=key, field='key', value=key)
        cloudfunc.run('setField', key=key, field='price', value=item[1])
        cloudfunc.run('setField', key=key, field='wish_price', value=item[2])
        cloudfunc.run('setField', key=key, field='type', value=item[3])
        cloudfunc.run('setField', key=key, field='name', value=item[4])
        cloudfunc.run('setField', key=key, field='image', value=item[5])
        cloudfunc.run('setField', key=key, field='seller', value=seller)
        push_sub_sub_list = cloudfunc.run('rpush', key='list_wish_lottery', value=key)


def msg_to_json(ty, name, data, appid, path, content, image):
    seller = {}
    seller['type'] = ty  # 0.推荐的是小程序  1.推荐的是群二维码
    seller['name'] = name  # 名称
    seller['data'] = data  # 需要传输的数据
    seller['appid'] = appid  # 小程序码   或者   微信号码
    seller['path'] = path  # 路径
    seller['content'] = content  # 具体的内容
    seller['image'] = image  # 具体的内容
    return json.dumps(seller)

def main():
    load_lottery_item(url)

main()