get_list_details_new(key,begin,end) #查询一个列表下的所有详情
send_wish_tapad(uid,code)  #用户光看广告送积分
ad_lottery(uid,gid,code)    #点击广告抽奖
wish_lottery(uid,gid,code,groupid,sharer)   # 积分抽奖
query_user_field(uid,code,field) #查询用户的某些信息
wish_exchange(uid,code) #积分兑换
send_subscribe_message(uid, programid, data) #给用户发送服务通知

create_handsel(uid,goodid) #创建砍单
update_handsel(handsel_key,uid,new_user,code,groupid)#砍价
handsel_quicken(key)#用200积分给砍价加速

accept_order(accept_order)#确认订单
invitation_code(code,user)  #邀请码登录
set_invitation_code(code,user) #用户设置自己的邀请码

login(app_name,sharer,code) #注册/登录
getMiniQRCode(scene,page,type,programid) #  获取小程序码
set_user_info()#设置用户信息
get_user_info()#查询用户信息
getPhoneNumber()    #解密用户的手机号码
get_group_id()  #   获取群id

setString(key,value)
setExpireTime(key,value)#
getValue(key)
setField(key,field,value)
getField(key,field)
increField(key,field,value)
getHash(key)
hasField(key,field)
getListItemHash(key) #keys模糊查询
get_list_hash(key)
getListItemString(key) #keys模糊查询
getListAmount(key)#模糊查询数量
setSet(key,value)# 集合增加一个值
delSet(key,value) #删除集合中的一个元素
getSet(key)#集合中取出所有值

existSet(key,value)#    查询集合中是否有某个值
get_set_item_strings(key) #取出集合中的值
get_set_item_hash(key) #取出集合中的值
get_set_item_set(key)

rpush(key,value) #数组结尾增加一个值
lpush(key, value)  #数组第一个位置增加一个值
get_list_details(key,begin,end) #数组中查出数据
get_list_details_strings(key, begin, end)  #数组中查出数据
get_list_details_json_value(key,begin,end)
keys(key)
query_keys_amount(key)
scan(key,index,count,key_type)

del_key(key)
del_one_key(key)
query_list(key,begin,end)