# Crewing 自动注册
import requests
import json
import csv
import time
url = "http://mol.uat.emarineonline.com/api/crewing/user/register?client=CREWC-IOS-CHINA"
sleep_ = 10
def login(email,nickname):
    payload = {
        'identifier': email,
        'nickname': nickname,
        'password': 'Aa123456',
        'platform': 'WEB',
        'autoLogin': False,
        'emailTemplateName': 'crewing.account.register.ok'
    }
    r = requests.post(url, data=json.dumps(payload), headers={
                    'Content-Type': 'application/json'})
    print(r.content)

f = open('/Users/pharaon/projects/python/user.csv', 'r')
csv_file = csv.reader(f)
for item in csv_file:
    time.sleep(sleep_)
    login(item[0],item[1])


# if __name__ == "__main__":
#     



