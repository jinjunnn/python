import csv
import requests
import leancloud
from leancloud import cloudfunc
from io import StringIO
leancloud.init(
    "0EaEC5sQIVi9vLFPkeWwLoPN-gzGzoHsz", master_key="NCjeEh0PTMAiY43KWWk6ks1T")


# 查询所有用户
ge = cloudfunc.run('keys', key='user_*')
for item in ge:
    user = cloudfunc.run('getHash', key=item)
    print(
        user.get('uid', ''), user.get('nickName', ''), user.get(
            'f_balance', ''), user.get('image', ''), user.get('objectid', ''))
