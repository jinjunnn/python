import csv
import pandas as pd
import numpy as np

share = pd.read_csv('/Users/jinjun/project/python/600833.SH.csv', index_col=0)




count = 0   #统计阿龙指标
up_index = 70   # 阿龙指标 up值
down_index = 40 # 阿龙指标 down值

# 阿龙指标策略 1：符合策略，-1：不符合策略，0：不符合策略
def strategy_one(up,down):
    if up > up_index and down < down_index:
        return 1
    elif up < down_index and up_index < down:
        return -1
    else:
        return 0

#   顺势指标策略
def cal_z_status(row):
    if row['顺势指标x'] == row['顺势指标x-shift']:
        return 0
    if (row['顺势指标x'] == 1 and row['顺势指标x-shift'] == 0) or  (row['顺势指标x'] == 1 and row['顺势指标x-shift'] == -1)  or (row['顺势指标x'] == 0 and row['顺势指标x-shift'] == -1):
        return 1
    elif  (row['顺势指标x'] == 0 and row['顺势指标x-shift'] == 1) or  (row['顺势指标x'] == -1 and row['顺势指标x-shift'] == 0)  or (row['顺势指标x'] == -1 and row['顺势指标x-shift'] == 1):
        return -1
    else:
        return 100
        

#统计阿龙指标在某一个周期持续的时间
def count_position(row):
    if row['aroon_up_dates'] == row['aloon_shift-1']:
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
        try:
            result = share.loc[row.name + 30:row.name, 'close']
            print(result.max(),share.loc[row.name, 'close'])
        except:
            pass
        
    else:
        return 0

#计算 X 位置
def cal_x_position(row):
    if row['顺势指标'] > 100:
        return 1
    elif row['顺势指标'] > -100 and row['顺势指标'] < 100:
        return 0
    else:
        return -1
    

#计算 Y 位置
def cal_y_position(row):
    if row['顺势指标x'] > row['顺势指标shift'] :
        return 1
    elif row['顺势指标x'] < row['顺势指标shift']:
        return -1
    else:
        return 0


# 阿龙指数 up越大越好，down越小越好； 我们这里设置阿龙指数的up和down为0.5，即up和down的范围为-0.5~0.5
def aroon_position():
    share['aroon_up_dates'] = share.apply(lambda x: strategy_one(x['阿隆指标up'],x['阿隆指标down']),axis=1) #阿隆指标是否符合策略 1：符合策略，-1：不符合策略，0：不符合策略
    share['aloon_shift-1'] = share['aroon_up_dates'].shift(1) # 前一天周期的结果
    share['count_aloon_position'] = share.apply(count_position,axis=1)  # 统计阿龙指标在某一个周期持续的时间

    share['aloon_max'] = share.apply(aloon_max,axis=1) #阿隆指标的最大值
    share['顺势指标shift'] = share['顺势指标'].shift(1) # 前一天周期的结果
    share['顺势指标x'] = share.apply(cal_x_position,axis=1) # 顺势指标策略
    share['顺势指标x-shift'] = share['顺势指标x'].shift(1) # 前一天周期的结果
    share['顺势指标y'] = share.apply(cal_y_position,axis=1) # 前一天周期的结果
    share['顺势指标z_status'] = share.apply(cal_z_status,axis=1) # 前一天周期的结果
    share.to_csv('123.csv')
    # position = share.loc[:, '阿隆指标down']
    # for item in position:
    #     print(item)



aroon_position()



#pandas取最后10个数据
# result = share.tail(10) # 取最后10个数据


