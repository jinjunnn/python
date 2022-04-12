# Crewing 自动注册
import requests
import json
import csv
import time
url = "https://www.ecrewingonline.com/api/crewing/user/register?client=CREWC-IOS-CHINA"

sleep_ = 1
def login(email,nickname,send_email):
    payload = {
        'identifier': email,
        'nickname': nickname,
        'password': 'Aa123456',
        'platform': 'WEB',
        'autoLogin': False,
        'emailTemplateName': send_email
    }
    print(payload)
    r = requests.post(url, data=json.dumps(payload), headers={
                    'Content-Type': 'application/json'})
    print(r.content)

f = open('/Users/pharaon/projects/python/4月第一周.csv', 'r')
csv_file = csv.reader(f)
for item in csv_file:
    time.sleep(sleep_)
    if item[0]=='1' :
        login(item[1],item[2],'crewing.account.register.ok')
    else :
        login(item[1],item[2],'None')
# if __name__ == "__main__":
#     



