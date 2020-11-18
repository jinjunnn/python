# 上传本地文件
# import oss2

# auth = oss2.Auth('LTAImlDNxFXoUu5b', 'cfYkpIxprJVdW6xpJ9l6D34xHIw9n8')
# bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com',
#                      'oneshenzhen')
# # <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
# bucket.put_object_from_file('http://oss-cn-shenzhen.aliyuncs.com', '<yourLocalFile>')


# -*- coding: utf-8 -*-
import oss2
import requests

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAImlDNxFXoUu5b', 'cfYkpIxprJVdW6xpJ9l6D34xHIw9n8')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com',
                     'oneshenzhen')
# requests.get返回的是一个可迭代对象（Iterable），此时Python SDK会通过Chunked Encoding方式上传。
input = requests.get('http://www.aliyun.com')
bucket.put_object('shipin1', input)
