# 王者荣耀小程序发送模板消息
import requests
import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "WekN4hEaRUx0bLwhjdWqBIY8-gzGzoHsz", master_key="e7YCFNPESmWVH6pS4HiUlL4q")

payload = {
    'grant_type': 'client_credential',
    'appid': 'wx4f93ecdfd7367530',
    'secret': 'a66cd9b86fab0ef2187196f72d628726',
}
url = "https://api.weixin.qq.com/cgi-bin/token"


def get_access_token():
    headers = {"Accept-Encoding": "gzip", "Connection": "close"}
    r = requests.get(url, params=payload, headers=headers)
    json_obj = r.json()
    print(json_obj)


if __name__ == "__main__":
    get_access_token()