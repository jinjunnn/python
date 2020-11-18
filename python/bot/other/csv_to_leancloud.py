import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")


url = '/Users/mac/spader/download/sephora_china.csv'


def push_item_to_list():
    f = open(url, 'r')
    csv_file = csv.reader(f)

    for i in csv_file:
        Sephora = leancloud.Object.extend('Sephora')
        goods = Sephora()
        goods.set('brand', i[0])
        goods.set('name', i[1])
        goods.set('image', i[2])
        goods.set('link', i[3])

        goods.save()

push_item_to_list()