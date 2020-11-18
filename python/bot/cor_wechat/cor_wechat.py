#   企业微信
import requests
import json


Secret = "T7xyPLDynUJMYmdn7QVIUCIxucSWH8YrN_kMlsvWHsk"#权限密码，从客户联系-客户-api中获得
corpid = 'ww53a2033b1ba6382c'#公司账号
uid = 'JinJun'#管理员账号
#获取access_tokenapi






def get_access_token():
    #1.从access_token.json拿到数据，如果expired_at过期，则从新生成一个access_token并保存
    #2.然后将access_token 返回；
    #3.如果未过期，直接返回access_token
    url_get_token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
    # 上述功能未开发
    access_token_obj = requests.post(url=url_get_token.format(corpid, Secret))
    access_token = access_token_obj.json().get('access_token')
    return access_token


def get_custom_list():
    #获取外部联系人列表api
    access_token = get_access_token()
    url_get_custom_list = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list?access_token={}&userid={}'
    user_list_wrap = requests.get(url=url_get_custom_list.format(access_token, uid))
    return user_list_wrap.json().get('external_userid')

#   获取用户信息详情
def get_custom_infor(exid):
    #获取外部联系人信息api
    access_token = get_access_token()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get?access_token={}&external_userid={}'
    user_info_wrap = requests.get(url=url.format(access_token, exid))
    return (user_info_wrap.json().get('external_contact'))


user_info = get_custom_infor('wmODEuDQAApYlCHC_z7uh-Ia9cDrVsJQ')
for k, v in user_info.items():
    print(k,v)