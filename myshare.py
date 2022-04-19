import tushare as ts
import pandas as pd
import numpy as np
import datetime
import os
import sys
import time
import json
import requests
import csv
import re
import random
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import http.client
import http.cookiejar
import http.client
import http.cookiejar
import talib as ta

#设置tushare pro的token并获取连接
ts.set_token('eb257271b6dd38501c139f0dcf7ddb949990c4384cae1f821c566884')
token = 'eb257271b6dd38501c139f0dcf7ddb949990c4384cae1f821c566884'
pro = ts.pro_api(token)

#设置股票池
share = '600833.SH'
fileName = share + '.csv'

def data_calculation(dframe):
    df=dframe
    _open = df['open']
    ts_code = df['ts_code']
    trade_date = df['trade_date']
    high = df['high']
    low = df['low']
    close = df['close']
    pre_close = df['pre_close']
    change = df['change']
    pct_chg = df['pct_chg']
    volume = df['vol']
    amount = df['amount']

#以下为动量指标
    # # 平均趋向指数 ADX
    # df['平均趋向指数'] = ta.ADX(high, low, close, timeperiod=14)
    # #平均趋向指数的趋向指数
    # df['平均趋向指数的趋向指数'] = ta.ADXR(high, low, close, timeperiod=14)

    # 名称：阿隆指标
    # 简介：该指标是通过计算自价格达到近期最高值和最低值以来所经过的期间数，阿隆指标帮助你预测价格趋势到趋势区域（或者反过来，从趋势区域到趋势）的变化。
    df['阿隆指标down'], df['阿隆指标up'] = ta.AROON(high, low, timeperiod=17)  
    df['阿隆指标down'] = df['阿隆指标down'].fillna(1)
    df['阿隆指标up'] = df['阿隆指标up'].fillna(1)
    #     名称：顺势指标
    # 简介：CCI指标专门测量股价是否已超出常态分布范围
    df['顺势指标'] = ta.CCI(high, low, close, timeperiod=12) 
    df['顺势指标'] = df['顺势指标'].fillna(1)
#     # 函数名：CMO
#     # 名称：钱德动量摆动指标
#     # 简介：与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，钱德动量指标在计算公式的分子中采用上涨日和下跌日的数据。 计算公式：CMO=（Su－Sd）*100/（Su+Sd）
#     # 其中：Su是今日收盘价与昨日收盘价（上涨日）差值加总。若当日下跌，则增加值为0；Sd是今日收盘价与做日收盘价（下跌日）差值的绝对值加总。若当日上涨，则增加值为0；
#     # 本指标类似RSI指标。
#     # 当本指标下穿-50水平时是买入信号，上穿+50水平是卖出信号。
#     # 钱德动量摆动指标的取值介于-100和100之间。
#     # 本指标也能给出良好的背离信号。
#     # 当股票价格创出新低而本指标未能创出新低时，出现牛市背离；
#     # 当股票价格创出新高而本指标未能创出新高时，当出现熊市背离时。
#     # 我们可以用移动均值对该指标进行平滑。
#     df['钱德动量摆动指标'] = ta.CMO(close, timeperiod=14)

#     # 函数名：DX
#     # 名称：动向指标或趋向指标
#     # 简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。
#     df['动向指标或趋向指标'] = ta.DX(high, low, close, timeperiod=14)

#     # 函数名：MFI
#     # 名称：资金流量指标
#     # 简介：属于量价类指标，反映市场的运行趋势
#     df['资金流量指标'] = ta.MFI(high, low, close, volume, timeperiod=14)

#     # 函数名：DMI 中的DI指标 负方向指标
#     # 名称：下升动向值
#     # 简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。
#     df['下升动向值'] = ta.MINUS_DI(high, low, close, timeperiod=14)

#     # 函数名：MINUS_DM
#     # 名称： 上升动向值 DMI中的DM代表正趋向变动值即上升动向值
#     # 简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。
#     df['上升动向值 DMI'] = ta.MINUS_DM(high, low, timeperiod=14)

#     # 函数名：MOM
#     # 名称： 上升动向值
#     # 简介：投资学中意思为续航，指股票(或经济指数)持续增长的能力。研究发现，赢家组合在牛市中存在着正的动量效应，输家组合在熊市中存在着负的动量效应。
#     df['上升动向值'] = ta.MOM(close, timeperiod=14)

#     # 函数名：PPO 名称： 价格震荡百分比指数
#     # 简介：价格震荡百分比指标（PPO）是一个和MACD指标非常接近的指标。
#     # PPO标准设定和MACD设定非常相似：12,26,9和PPO，和MACD一样说明了两条移动平均线的差距，但是它们有一个差别是PPO是用百分比说明。
#     df['价格震荡百分比指数'] = ta.PPO(close, fastperiod=12, slowperiod=26, matype=0)

#     # 函数名：ROC
#     # 名称： 变动率指标
#     # 简介：ROC是由当天的股价与一定的天数之前的某一天股价比较，其变动速度的大小,来反映股票市变动的快慢程度
#     df['变动率指标'] = ta.ROC(close, timeperiod=14)

#     # 函数名：RSI
#     # 名称：相对强弱指数
#     # 简介：是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。
#     df['相对强弱指数'] = ta.RSI(close, timeperiod=14)

#     # 函数名：ULTOSC
#     # 名称：终极波动指标
#     # 简介：UOS是一种多方位功能的指标，除了趋势确认及超买超卖方面的作用之外，它的“突破”讯号不仅可以提供最适当的交易时机之外，更可以进一步加强指标的可靠度。
#     df['终极波动指标'] = ta.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)

#     # 函数名：WILLR
#     # 名称：威廉指标
#     # 简介：WMS表示的是市场处于超买还是超卖状态。股票投资分析方法主要有如下三种：基本分析、技术分析、演化分析。在实际应用中，它们既相互联系，又有重要区别。
#     df['威廉指标'] = ta.WILLR(high, low, close, timeperiod=14)



# #以下为量指标
#     # 函数名：AD
#     # 名称：Chaikin A/D Line 累积/派发线（Accumulation/Distribution Line）
#     # 简介：Marc Chaikin提出的一种平衡交易量指标，以当日的收盘价位来估算成交流量，用于估定一段时间内该证券累积的资金流量。
#     # 计算公式：
#     # A/D = 昨日A/D + 多空对比 * 今日成交量 多空对比 = [（收盘价- 最低价） - （最高价 - 收盘价）] / （最高价 - 最低价) 若最高价等于最低价： 多空对比 = （收盘价 / 昨收盘） - 1
#     # 研判：
#     # 1、A/D测量资金流向，向上的A/D表明买方占优势，而向下的A/D表明卖方占优势
#     # 2、A/D与价格的背离可视为买卖信号，即底背离考虑买入，顶背离考虑卖出
#     # 3、应当注意A/D忽略了缺口的影响，事实上，跳空缺口的意义是不能轻易忽略的
#     # A/D指标无需设置参数，但在应用时，可结合指标的均线进行分析
#     df['累积/派发线'] = ta.AD(high, low, close, volume)

#     # 函数名：ADOSC
#     # 名称：Chaikin A/D Oscillator Chaikin震荡指标
#     # 简介：将资金流动情况与价格行为相对比，检测市场中资金流入和流出的情况
#     # 计算公式：fastperiod A/D - slowperiod A/D
#     # 研判：
#     # 1、交易信号是背离：看涨背离做多，看跌背离做空
#     # 2、股价与90天移动平均结合，与其他指标结合
#     # 3、由正变负卖出，由负变正买进
#     df['震荡指标'] = ta.AD(high, low, close, volume)    

#     # 函数名：ADOSC
#     # 名称：Chaikin A/D Oscillator Chaikin震荡指标
#     # 简介：将资金流动情况与价格行为相对比，检测市场中资金流入和流出的情况
#     # 计算公式：fastperiod A/D - slowperiod A/D
#     # 研判：
#     # 1、交易信号是背离：看涨背离做多，看跌背离做空
#     # 2、股价与90天移动平均结合，与其他指标结合
#     # 3、由正变负卖出，由负变正买进
#     df['震荡指标'] = ta.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)

#     # 函数名：OBV
#     # 名称：On Balance Volume 能量潮
#     # 简介：Joe Granville提出，通过统计成交量变动的趋势推测股价趋势
#     # 计算公式：以某日为基期，逐日累计每日上市股票总成交量，若隔日指数或股票上涨 ，则基期OBV加上本日成交量为本日OBV。隔日指数或股票下跌， 则基期OBV减去本日成交量为本日OBV
#     # 研判：
#     # 1、以“N”字型为波动单位，一浪高于一浪称“上升潮”，下跌称“跌潮”；上升潮买进，跌潮卖出
#     # 2、须配合K线图走势
#     # 3、用多空比率净额法进行修正，但不知TA-Lib采用哪种方法
#     df['能量潮'] = ta.OBV(close, volume)


# # 波动性指标
#     # 函数名：ATR
#     # 名称：真实波动幅度均值
#     # 简介：真实波动幅度均值（ATR)是 以 N 天的指数移动平均数平均後的交易波动幅度。 计算公式：一天的交易幅度只是单纯地 最大值 - 最小值。
#     # 而真实波动幅度则包含昨天的收盘价，若其在今天的幅度之外：
#     # 真实波动幅度 = max(最大值,昨日收盘价) − min(最小值,昨日收盘价) 真实波动幅度均值便是「真实波动幅度」的 N 日 指数移动平均数。
#     # 特性：：
#     # 波动幅度的概念表示可以显示出交易者的期望和热情。
#     # 大幅的或增加中的波动幅度表示交易者在当天可能准备持续买进或卖出股票。
#     # 波动幅度的减少则表示交易者对股市没有太大的兴趣。
#     df['真实波动幅度均值'] = ta.ATR(high, low, close, timeperiod=14)

#     # 函数名：NATR
#     # 名称：归一化波动幅度均值
#     # 简介：归一化波动幅度均值（NATR)是
#     df['归一化波动幅度均值'] = ta.NATR(high, low, close, timeperiod=14)    


#     # 函数名：TRANGE
#     # 名称：真正的范围
#     df['真正的范围'] = ta.TRANGE(high, low, close)

# #价格指标
#     # 函数名：WCLPRICE
#     # 名称：加权收盘价
#     df['加权收盘价'] = ta.WCLPRICE(high, low, close)

# #周期类函数
#     # 函数名：HT_DCPERIOD
#     # 名称： 希尔伯特变换-主导周期
#     # 简介：将价格作为信息信号，计算价格处在的周期的位置，作为择时的依据。
#     df['希尔伯特变换-主导周期'] = ta.HT_DCPERIOD(close)

# #形态识别
#     #     函数名：CDL2CROWS
#     # 名称：Two Crows 两只乌鸦
#     # 简介：三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴， 收盘比前一日收盘价低，预示股价下跌。
#     df['两只乌鸦'] = ta.CDL2CROWS(_open, high, low, close)


#     # 函数名：CDL3BLACKCROWS
#     # 名称：Three Black Crows 三只乌鸦
#     # 简介：三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价， 每日开盘价都在上根K线实体内，预示股价下跌。
#     df['三只乌鸦'] = ta.CDL3BLACKCROWS(_open, high, low, close)


#     # 函数名：CDL3INSIDE
#     # 名称： Three Inside Up/Down 三内部上涨和下跌
#     # 简介：三日K线模式，母子信号+长K线，以三内部上涨为例，K线为阴阳阳， 第三天收盘价高于第一天开盘价，第二天K线在第一天K线内部，预示着股价上涨。
#     df['三内部上涨和下跌'] = ta.CDL3INSIDE(_open, high, low, close)


#     # 函数名：CDL3LINESTRIKE
#     # 名称： Three-Line Strike 三线打击
#     # 简介：四日K线模式，前三根阳线，每日收盘价都比前一日高， 开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。
#     df['三线打击'] = ta.CDL3LINESTRIKE(_open, high, low, close)


#     # 函数名：CDL3OUTSIDE
#     # 名称：Three Outside Up/Down 三外部上涨和下跌
#     # 简介：三日K线模式，与三内部上涨和下跌类似，K线为阴阳阳，但第一日与第二日的K线形态相反， 以三外部上涨为例，第一日K线在第二日K线内部，预示着股价上涨。
#     df['三外部上涨和下跌'] = ta.CDL3OUTSIDE(_open, high, low, close)


#     # 函数名：CDL3STARSINSOUTH
#     # 名称：Three Stars In The South 南方三星
#     # 简介：三日K线模式，与大敌当前相反，三日K线皆阴，第一日有长下影线， 第二日与第一日类似，K线整体小于第一日，第三日无下影线实体信号， 成交价格都在第一日振幅之内，预示下跌趋势反转，股价上升。
#     df['南方三星'] = ta.CDL3STARSINSOUTH(_open, high, low, close)


#     # 函数名：CDL3WHITESOLDIERS
#     # 名称：Three Advancing White Soldiers 三个白兵
#     # 简介：三日K线模式，三日K线皆阳， 每日收盘价变高且接近最高价，开盘价在前一日实体上半部，预示股价上升。
#     df['三个白兵'] = ta.CDL3WHITESOLDIERS(_open, high, low, close)


#     # 函数名：CDLABANDONEDBABY
#     # 名称：Abandoned Baby 弃婴
#     # 简介：三日K线模式，第二日价格跳空且收十字星（开盘价与收盘价接近， 最高价最低价相差不大），预示趋势反转，发生在顶部下跌，底部上涨。
#     df['弃婴'] = ta.CDLABANDONEDBABY(_open, high, low, close, penetration=0)



#     # 函数名：CDLADVANCEBLOCK
#     # 名称：Advance Block 大敌当前
#     # 简介：三日K线模式，三日都收阳，每日收盘价都比前一日高， 开盘价都在前一日实体以内，实体变短，上影线变长。
#     df['大敌当前'] = ta.CDLADVANCEBLOCK(_open, high, low, close)


#     # 函数名：CDLBELTHOLD
#     # 名称：Belt-hold 捉腰带线
#     # 简介：两日K线模式，下跌趋势中，第一日阴线， 第二日开盘价为最低价，阳线，收盘价接近最高价，预示价格上涨。
#     df['捉腰带线'] = ta.CDLBELTHOLD(_open, high, low, close)


#     # 函数名：CDLBREAKAWAY
#     # 名称：Breakaway 脱离
#     # 简介：五日K线模式，以看涨脱离为例，下跌趋势中，第一日长阴线，第二日跳空阴线，延续趋势开始震荡， 第五日长阳线，收盘价在第一天收盘价与第二天开盘价之间，预示价格上涨。
#     df['脱离'] = ta.CDLBREAKAWAY(_open, high, low, close)


#     # 函数名：CDLCLOSINGMARUBOZU
#     # 名称：Closing Marubozu 收盘缺影线
#     # 简介：一日K线模式，以阳线为例，最低价低于开盘价，收盘价等于最高价， 预示着趋势持续。
#     df['收盘缺影线'] = ta.CDLCLOSINGMARUBOZU(_open, high, low, close)


#     # 函数名：CDLCONCEALBABYSWALL
#     # 名称： Concealing Baby Swallow 藏婴吞没
#     # 简介：四日K线模式，下跌趋势中，前两日阴线无影线 ，第二日开盘、收盘价皆低于第二日，第三日倒锤头， 第四日开盘价高于前一日最高价，收盘价低于前一日最低价，预示着底部反转。
#     df['藏婴吞没'] = ta.CDLCONCEALBABYSWALL(_open, high, low, close)


#     # 函数名：CDLCOUNTERATTACK
#     # 名称：Counterattack 反击线
#     # 简介：二日K线模式，与分离线类似。
#     df['反击线'] = ta.CDLCOUNTERATTACK(_open, high, low, close)


#     # 函数名：CDLDARKCLOUDCOVER
#     # 名称：Dark Cloud Cover 乌云压顶
#     # 简介：二日K线模式，第一日长阳，第二日开盘价高于前一日最高价， 收盘价处于前一日实体中部以下，预示着股价下跌。
#     df['乌云压顶'] = ta.CDLDARKCLOUDCOVER(_open, high, low, close, penetration=0)


#     # 函数名：CDLDOJI
#     # 名称：Doji 十字
#     # 简介：一日K线模式，开盘价与收盘价基本相同。
#     df['十字'] = ta.CDLDOJI(_open, high, low, close)


#     # 函数名：CDLDOJISTAR
#     # 名称：Doji Star 十字星
#     # 简介：一日K线模式，开盘价与收盘价基本相同，上下影线不会很长，预示着当前趋势反转。
#     df['十字星'] = ta.CDLDOJISTAR(_open, high, low, close)


#     # 函数名：CDLDRAGONFLYDOJI
#     # 名称：Dragonfly Doji 蜻蜓十字/T形十字
#     # 简介：一日K线模式，开盘后价格一路走低， 之后收复，收盘价与开盘价相同，预示趋势反转。
#     df['蜻蜓十字/T形十字'] = ta.CDLDRAGONFLYDOJI(_open, high, low, close)


#     # 函数名：CDLENGULFING
#     # 名称：Engulfing Pattern 吞噬模式
#     # 简介：两日K线模式，分多头吞噬和空头吞噬，以多头吞噬为例，第一日为阴线， 第二日阳线，第一日的开盘价和收盘价在第二日开盘价收盘价之内，但不能完全相同。
#     df['吞噬模式'] = ta.CDLENGULFING(_open, high, low, close)


#     # 函数名：CDLEVENINGDOJISTAR
#     # 名称：Evening Doji Star 十字暮星
#     # 简介：三日K线模式，基本模式为暮星，第二日收盘价和开盘价相同，预示顶部反转。
#     df['十字暮星'] = ta.CDLEVENINGDOJISTAR(_open, high, low, close, penetration=0)


#     # 函数名：CDLEVENINGSTAR
#     # 名称：Evening Star 暮星
#     # 简介：三日K线模式，与晨星相反，上升趋势中, 第一日阳线，第二日价格振幅较小，第三日阴线，预示顶部反转。
#     df['暮星'] = ta.CDLEVENINGSTAR(_open, high, low, close, penetration=0)


#     # 函数名：CDLGAPSIDESIDEWHITE
#     # 名称：Up/Down-gap side-by-side white lines 向上/下跳空并列阳线
#     # 简介：二日K线模式，上升趋势向上跳空，下跌趋势向下跳空, 第一日与第二日有相同开盘价，实体长度差不多，则趋势持续。
#     df['向上/下跳空并列阳线'] = ta.CDLGAPSIDESIDEWHITE(_open, high, low, close)



#     # 函数名：CDLGRAVESTONEDOJI
#     # 名称：Gravestone Doji 墓碑十字/倒T十字
#     # 简介：一日K线模式，开盘价与收盘价相同，上影线长，无下影线，预示底部反转。
#     df['墓碑十字/倒T十字'] = ta.CDLGRAVESTONEDOJI(_open, high, low, close)


#     # 函数名：CDLHAMMER
#     # 名称：Hammer 锤头
#     # 简介：一日K线模式，实体较短，无上影线， 下影线大于实体长度两倍，处于下跌趋势底部，预示反转。
#     df['锤头'] = ta.CDLHAMMER(_open, high, low, close)


#     # 函数名：CDLHANGINGMAN
#     # 名称：Hanging Man 上吊线
#     # 简介：一日K线模式，形状与锤子类似，处于上升趋势的顶部，预示着趋势反转。
#     df['上吊线'] = ta.CDLHANGINGMAN(_open, high, low, close)


#     # 函数名：CDLHARAMI
#     # 名称：Harami Pattern 母子线
#     # 简介：二日K线模式，分多头母子与空头母子，两者相反，以多头母子为例，在下跌趋势中，第一日K线长阴， 第二日开盘价收盘价在第一日价格振幅之内，为阳线，预示趋势反转，股价上升。
#     df['母子线'] = ta.CDLHARAMI(_open, high, low, close)


#     # 函数名：CDLHARAMICROSS
#     # 名称：Harami Cross Pattern 十字孕线
#     # 简介：二日K线模式，与母子县类似，若第二日K线是十字线， 便称为十字孕线，预示着趋势反转。
#     df['十字孕线'] = ta.CDLHARAMICROSS(_open, high, low, close)


#     # 函数名：CDLHIGHWAVE
#     # 名称：High-Wave Candle 风高浪大线
#     # 简介：三日K线模式，具有极长的上/下影线与短的实体，预示着趋势反转。
#     df['风高浪大线'] = ta.CDLHIGHWAVE(_open, high, low, close)


#     # 函数名：CDLHIKKAKE
#     # 名称：Hikkake Pattern 陷阱
#     # 简介：三日K线模式，与母子类似，第二日价格在前一日实体范围内, 第三日收盘价高于前两日，反转失败，趋势继续。
#     df['陷阱'] = ta.CDLHIKKAKE(_open, high, low, close)


#     # 函数名：CDLHIKKAKEMOD
#     # 名称：Modified Hikkake Pattern 修正陷阱
#     # 简介：三日K线模式，与陷阱类似，上升趋势中，第三日跳空高开； 下跌趋势中，第三日跳空低开，反转失败，趋势继续。
#     df['修正陷阱'] = ta.CDLHIKKAKEMOD(_open, high, low, close)


#     # 函数名：CDLHOMINGPIGEON
#     # 名称：Homing Pigeon 家鸽
#     # 简介：二日K线模式，与母子线类似，不同的的是二日K线颜色相同， 第二日最高价、最低价都在第一日实体之内，预示着趋势反转。
#     df['家鸽'] = ta.CDLHOMINGPIGEON(_open, high, low, close)


#     # 函数名：CDLIDENTICAL3CROWS
#     # 名称：Identical Three Crows 三胞胎乌鸦
#     # 简介：三日K线模式，上涨趋势中，三日都为阴线，长度大致相等， 每日开盘价等于前一日收盘价，收盘价接近当日最低价，预示价格下跌。
#     df['三胞胎乌鸦'] = ta.CDLIDENTICAL3CROWS(_open, high, low, close)


#     # 函数名：CDLINNECK
#     # 名称：In-Neck Pattern 颈内线
#     # 简介：二日K线模式，下跌趋势中，第一日长阴线， 第二日开盘价较低，收盘价略高于第一日收盘价，阳线，实体较短，预示着下跌继续。
#     df['颈内线'] = ta.CDLINNECK(_open, high, low, close)


#     # 函数名：CDLINVERTEDHAMMER
#     # 名称：Inverted Hammer 倒锤头
#     # 简介：一日K线模式，上影线较长，长度为实体2倍以上， 无下影线，在下跌趋势底部，预示着趋势反转。
#     df['倒锤头'] = ta.CDLINVERTEDHAMMER(_open, high, low, close)


#     # 函数名：CDLKICKING
#     # 名称：Kicking 反冲形态
#     # 简介：二日K线模式，与分离线类似，两日K线为秃线，颜色相反，存在跳空缺口。
#     df['反冲形态'] = ta.CDLKICKING(_open, high, low, close)


#     # 函数名：CDLKICKINGBYLENGTH
#     # 名称：Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态
#     # 简介：二日K线模式，与反冲形态类似，较长缺影线决定价格的涨跌。
#     df['由较长缺影线决定的反冲形态'] = ta.CDLKICKINGBYLENGTH(_open, high, low, close)


#     # 函数名：CDLLADDERBOTTOM
#     # 名称：Ladder Bottom 梯底
#     # 简介：五日K线模式，下跌趋势中，前三日阴线， 开盘价与收盘价皆低于前一日开盘、收盘价，第四日倒锤头，第五日开盘价高于前一日开盘价， 阳线，收盘价高于前几日价格振幅，预示着底部反转。
#     df['梯底'] = ta.CDLLADDERBOTTOM(_open, high, low, close)


#     #  函数名：CDLLONGLEGGEDDOJI
#     # 名称：Long Legged Doji 长脚十字
#     # 简介：一日K线模式，开盘价与收盘价相同居当日价格中部，上下影线长， 表达市场不确定性。   
#     df['长脚十字'] = ta.CDLLONGLEGGEDDOJI(_open, high, low, close)



#     #     函数名：CDLLONGLINE
#     # 名称：Long Line Candle 长蜡烛
#     # 简介：一日K线模式，K线实体长，无上下影线。
#     df['长蜡烛'] = ta.CDLLONGLINE(_open, high, low, close)


#     #     函数名：CDLMARUBOZU
#     # 名称：Marubozu 光头光脚/缺影线
#     # 简介：一日K线模式，上下两头都没有影线的实体， 阴线预示着熊市持续或者牛市反转，阳线相反。
#     df['光头光脚/缺影线'] = ta.CDLMARUBOZU(_open, high, low, close)


#     # 函数名：CDLMATCHINGLOW
#     # 名称：Matching Low 相同低价
#     # 简介：二日K线模式，下跌趋势中，第一日长阴线， 第二日阴线，收盘价与前一日相同，预示底部确认，该价格为支撑位。
#     df['相同低价'] = ta.CDLMATCHINGLOW(_open, high, low, close)


#     #     函数名：CDLMATHOLD
#     # 名称：Mat Hold 铺垫
#     # 简介：五日K线模式，上涨趋势中，第一日阳线，第二日跳空高开影线， 第三、四日短实体影线，第五日阳线，收盘价高于前四日，预示趋势持续。
#     df['铺垫'] = ta.CDLMATHOLD(_open, high, low, close, penetration=0)


#     # 函数名：CDLMORNINGDOJISTAR
#     # 名称：Morning Doji Star 十字晨星
#     # 简介：三日K线模式， 基本模式为晨星，第二日K线为十字星，预示底部反转。
#     df['十字晨星'] = ta.CDLMORNINGDOJISTAR(_open, high, low, close, penetration=0)


#     #     函数名：CDLMORNINGSTAR
#     # 名称：Morning Star 晨星
#     # 简介：三日K线模式，下跌趋势，第一日阴线， 第二日价格振幅较小，第三天阳线，预示底部反转。
#     df['晨星'] = ta.CDLMORNINGSTAR(_open, high, low, close, penetration=0)


#     # 函数名：CDLONNECK
#     # 名称：On-Neck Pattern 颈上线
#     # 简介：二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低， 收盘价与前一日最低价相同，阳线，实体较短，预示着延续下跌趋势。
#     df['颈上线'] = ta.CDLONNECK(_open, high, low, close)


#     #     函数名：CDLPIERCING
#     # 名称：Piercing Pattern 刺透形态
#     # 简介：两日K线模式，下跌趋势中，第一日阴线，第二日收盘价低于前一日最低价， 收盘价处在第一日实体上部，预示着底部反转。
#     df['刺透形态'] = ta.CDLPIERCING(_open, high, low, close)


#     # 函数名：CDLRICKSHAWMAN
#     # 名称：Rickshaw Man 黄包车夫
#     # 简介：一日K线模式，与长腿十字线类似， 若实体正好处于价格振幅中点，称为黄包车夫。
#     df['黄包车夫'] = ta.CDLRICKSHAWMAN(_open, high, low, close)


#     # 函数名：CDLRISEFALL3METHODS 名称：Rising/Falling Three Methods 上升/下降三法
#     # 简介： 五日K线模式，以上升三法为例，上涨趋势中， 第一日长阳线，中间三日价格在第一日范围内小幅震荡， 第五日长阳线，收盘价高于第一日收盘价，预示股价上升。
#     df['上升/下降三法'] = ta.CDLRISEFALL3METHODS(_open, high, low, close)


#     # 函数名：CDLSEPARATINGLINES
#     # 名称：Separating Lines 分离线
#     # 简介：二日K线模式，上涨趋势中，第一日阴线，第二日阳线， 第二日开盘价与第一日相同且为最低价，预示着趋势继续。
#     df['分离线'] = ta.CDLSEPARATINGLINES(_open, high, low, close)


#     # 函数名：CDLSHOOTINGSTAR
#     # 名称：Shooting Star 射击之星
#     # 简介：一日K线模式，上影线至少为实体长度两倍， 没有下影线，预示着股价下跌
#     df['射击之星'] = ta.CDLSHOOTINGSTAR(_open, high, low, close)


#     # 函数名：CDLSHORTLINE
#     # 名称：Short Line Candle 短蜡烛
#     # 简介：一日K线模式，实体短，无上下影线
#     df['短蜡烛'] = ta.CDLSHORTLINE(_open, high, low, close)


#     # 函数名：CDLSPINNINGTOP
#     # 名称：Spinning Top 纺锤
#     # 简介：一日K线，实体小。
#     df['纺锤'] = ta.CDLSPINNINGTOP(_open, high, low, close)


#     # 函数名：CDLSTALLEDPATTERN
#     # 名称：Stalled Pattern 停顿形态
#     # 简介：三日K线模式，上涨趋势中，第二日长阳线， 第三日开盘于前一日收盘价附近，短阳线，预示着上涨结束
#     df['停顿形态'] = ta.CDLSTALLEDPATTERN(_open, high, low, close)


#     # 函数名：CDLSTICKSANDWICH
#     # 名称：Stick Sandwich 条形三明治
#     # 简介：三日K线模式，第一日长阴线，第二日阳线，开盘价高于前一日收盘价， 第三日开盘价高于前两日最高价，收盘价于第一日收盘价相同。
#     df['条形三明治'] = ta.CDLSTICKSANDWICH(_open, high, low, close)


#     # 函数名：CDLTAKURI
#     # 名称：Takuri (Dragonfly Doji with very long lower shadow) 探水竿
#     # 简介：一日K线模式，大致与蜻蜓十字相同，下影线长度长。
#     df['探水竿'] = ta.CDLTAKURI(_open, high, low, close)


#     # 函数名：CDLTASUKIGAP
#     # 名称：Tasuki Gap 跳空并列阴阳线
#     # 简介：三日K线模式，分上涨和下跌，以上升为例， 前两日阳线，第二日跳空，第三日阴线，收盘价于缺口中，上升趋势持续。
#     df['跳空并列阴阳线'] = ta.CDLTASUKIGAP(_open, high, low, close)


#     # 函数名：CDLTHRUSTING
#     # 名称：Thrusting Pattern 插入
#     # 简介：二日K线模式，与颈上线类似，下跌趋势中，第一日长阴线，第二日开盘价跳空， 收盘价略低于前一日实体中部，与颈上线相比实体较长，预示着趋势持续。
#     df['插入'] = ta.CDLTHRUSTING(_open, high, low, close)


#     # 函数名：CDLTRISTAR
#     # 名称：Tristar Pattern 三星
#     # 简介：三日K线模式，由三个十字组成， 第二日十字必须高于或者低于第一日和第三日，预示着反转。
#     df['三星'] = ta.CDLTRISTAR(_open, high, low, close)


#     # 函数名：CDLUNIQUE3RIVER
#     # 名称：Unique 3 River 奇特三河床
#     # 简介：三日K线模式，下跌趋势中，第一日长阴线，第二日为锤头，最低价创新低，第三日开盘价低于第二日收盘价，收阳线， 收盘价不高于第二日收盘价，预示着反转，第二日下影线越长可能性越大。
#     df['奇特三河床'] = ta.CDLUNIQUE3RIVER(_open, high, low, close)


#     # 函数名：CDLUPSIDEGAP2CROWS
#     # 名称：Upside Gap Two Crows 向上跳空的两只乌鸦
#     # 简介：三日K线模式，第一日阳线，第二日跳空以高于第一日最高价开盘， 收阴线，第三日开盘价高于第二日，收阴线，与第一日比仍有缺口。
#     df['向上跳空的两只乌鸦'] = ta.CDLUPSIDEGAP2CROWS(_open, high, low, close)


#     # 函数名：CDLXSIDEGAP3METHODS
#     # 名称：Upside/Downside Gap Three Methods 上升/下降跳空三法
#     # 简介：五日K线模式，以上升跳空三法为例，上涨趋势中，第一日长阳线，第二日短阳线，第三日跳空阳线，第四日阴线，开盘价与收盘价于前两日实体内， 第五日长阳线，收盘价高于第一日收盘价，预示股价上升。
#     df['上升/下降跳空三法'] = ta.CDLXSIDEGAP3METHODS(_open, high, low, close)
    df.to_csv(fileName)

#tushare获取股票数据
# ,ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount
def get_stock_data(share):
    df = pro.query('daily', ts_code=share, start_date='20090101', end_date='20220318')
    data_calculation(df.iloc[::-1])

get_stock_data(share)




#查询所有股票代码
def get_stock_basic():
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv('sharelist.csv')
# get_stock_basic()


# 查询分钟行情
def get_stock_min_exchange():
    df = ts.pro_bar(ts_code='600833.SH', start_date='2019-09-01 09:00:00', end_date='2019-09-01 13:45:00' ,freq='5min')
    df.to_csv('sharelist1.csv')

# get_stock_min_exchange()