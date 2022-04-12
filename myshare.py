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

#设置tushare pro的token并获取连接
token = '3278de1cbf0d4396105cad9a20060f98c96faa3ca04edb68ededf647'
pro = ts.pro_api(token)


#设置股票池
stock_pool = ['600833.SH']

#tushare获取股票数据
def get_stock_data(stock_pool):
    stock_data = pro.daily(ts_code=stock_pool, start_date='20220301', end_date='20220410')
    print(stock_data)
    return stock_data

get_stock_data(stock_pool)