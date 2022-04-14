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
#tushare获取股票数据
def get_stock_data(share):
    df = pro.query('daily', ts_code=share, start_date='20210701', end_date='20220318')
    print(df)
    df.to_csv(fileName)
# get_stock_data(share)


#查询所有股票代码
def get_stock_basic():
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv('sharelist.csv')
# get_stock_basic()


# 查询分钟行情
def get_stock_min_exchange():
    df = ts.pro_bar(ts_code='600833.SH', start_date='20220101', end_date='20220311' ,freq='D')
    # df.to_csv('sharelist1.csv')
    ta.
get_stock_min_exchange()