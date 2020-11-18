# 动态消息
import requests
import leancloud
from datetime import datetime
import json
import random

leancloud.init(
    "IGXFL8L08BMSNVGLyGhWr74I-gzGzoHsz", master_key="kOzll9KspLj58V55JhtM1Udv")

payload = {
    'access_token':
    '16_F8eEDdEd-_qhYmBOWRt7tKwo7pduo7NNR6DhHmyrwibiMCm1fXAYnUndWkLHjb4oc2NvW_6uLc2yO9qijZqAKyjGrCEk7o7rAe9QBHSWlB8wnHArvzzLq-6Ra0QgX4_R8N7wkIkzzrJJrcKjNZUeAFATFA',
}
url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/activityid/create"


def kaola():
    headers = {"Accept-Encoding": "gzip", "Connection": "close"}
    r = requests.get(url, params=payload, headers=headers)
    json_obj = r.json()
    print(json_obj)


if __name__ == "__main__":
    kaola()