import csv
import pandas as pd
import numpy as np

share = pd.read_csv('/Users/pharaon/projects/python/600833.SH.csv', index_col=0)


def done(up,down):
    if up > 70 and down < 30:
        return 1
    elif up < 30 and 70 < down:
        return -1
    else:
        return 0


def days_in_position(today,yestoday,days_in_position):
    print(today,yestoday,days_in_position)
    arr = []
    s = pd.Series(arr)
    if today == yestoday:
        print('same')
    else:
        print('not same')

# 阿龙指数 up越大越好，down越小越好； 我们这里设置阿龙指数的up和down为0.5，即up和down的范围为-0.5~0.5
def aroon_position():
    aroon_up = share['阿隆指标up'].fillna(1)
    aroon_down = share['阿隆指标down'].fillna(1)
    days_in_position = share['days_in_position'].fillna(0)
    share['elapsed'] = share.apply(lambda x: done(x['阿隆指标up'],x['阿隆指标down']),axis=1)
    share['aroon_up_dates'] = share.apply(lambda x: done(x['阿隆指标up'],x['阿隆指标down']),axis=1)
    share['aloon_shift-1'] = share['elapsed'].shift(-1)
    share['days_in_position'] = share.apply(lambda x: days_in_position(x['elapsed'],x['aloon_shift-1'],x['days_in_position']),axis=1)

    # share.to_csv('123.csv')
    # position = share.loc[:, '阿隆指标down']
    # for item in position:
    #     print(item)



aroon_position()



#pandas取最后10个数据
# result = share.tail(10) # 取最后10个数据


