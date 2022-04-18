import csv
import pandas as pd
import numpy as np

share = pd.read_csv('/Users/jinjun/project/python/123.csv', index_col=0)




count = 0
def done(up,down):
    if up > 70 and down < 30:
        return 1
    elif up < 30 and 70 < down:
        return -1
    else:
        return 0

def count_position(row):
    if row['elapsed'] == row['aloon_shift-1']:
        global count
        count = count + 1
        return count
    else:
        result = count + 1
        count = 0
        return result


# 阿隆指标的最大值
def aloon_max(row):
    if row['aroon_up_dates'] == 1 and row['count_aloon_position'] == 1:
        result = share.loc[row.name + 30:row.name, 'close']
        print(result.max(),share.loc[row.name, 'close'])
    else:
        return 0
    

# 阿龙指数 up越大越好，down越小越好； 我们这里设置阿龙指数的up和down为0.5，即up和down的范围为-0.5~0.5
def aroon_position():
    aroon_up = share['阿隆指标up'].fillna(1)
    aroon_down = share['阿隆指标down'].fillna(1)

    share['elapsed'] = share.apply(lambda x: done(x['阿隆指标up'],x['阿隆指标down']),axis=1)
    share['aroon_up_dates'] = share.apply(lambda x: done(x['阿隆指标up'],x['阿隆指标down']),axis=1)
    share['aloon_shift-1'] = share['elapsed'].shift(-1) # 前一天周期的结果
    share['count_aloon_position'] = share.apply(count_position,axis=1)

    share['aloon_max'] = share.apply(aloon_max,axis=1)
    share.to_csv('123.csv')
    # position = share.loc[:, '阿隆指标down']
    # for item in position:
    #     print(item)



aroon_position()



#pandas取最后10个数据
# result = share.tail(10) # 取最后10个数据


