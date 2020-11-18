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


list_name = 'list_handsel'
file_url = '/Users/mac/Library/Mobile Documents/com~apple~Numbers/Documents/resource/list/handsel.txt'
key = 'rpush'  #上传方式

def main():
    for item in open(file_url, encoding='utf-8').readlines():  # 逐行读取u
        result = cloudfunc.run(
            key, key=list_name, value='item_{}'.format(item).replace('\n', ''))


if __name__ == '__main__':
    main()