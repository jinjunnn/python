import requests
from bs4 import BeautifulSoup
import lxml
import html5lib
import ssl
from selenium import webdriver
import json
import time
import csv
import re
from googletrans import Translator

htmlfile = open(
    '/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/python/mk.htm',
    'r')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'lxml')

wrap = soup.find_all('div', class_='product-tile left large-6 small-6')
print(wrap[0])