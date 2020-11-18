# 贴吧自动回帖


from selenium import webdriver  # 导入网页内驱动模块
from selenium.webdriver.common.keys import Keys  # 导入按键类
from selenium.webdriver.common.action_chains import ActionChains  # 导入动作类
from random import choice
from time import sleep
import re
browser = webdriver.Firefox()  # 使用profile可以实现自动登录


def cookie():
    cookies = 'BIDUPSID=AA5BF47A3D5BE5D08A499830AD87F592; PSTM=1584003278; BAIDUID=AA5BF47A3D5BE5D0BDA752A2CCFD55B8:FG=1; H_WISE_SIDS=139913_143435_143879_144427_141744_144134_141901_142780_144482_144897_131861_131247_137745_144741_138883_141942_127969_140065_144337_140593_143060_141808_144607_141008_143471_144727_143923_131423_144289_128700_142207_144219_144004_107312_138596_139910_144105_143477_142426_142911_143548_144239_142113_143855_144098_140843_110085; BDUSS=FGVzVjZjc1c2RaTDZwNVhBZ0dJb2JBOVJXUDJUZmxIZFFkM3VMZWxkQmd5cmRlSVFBQUFBJCQAAAAAAAAAAAEAAAAbwfoveW91aXl5egAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA9kF5gPZBeN2; BDSFRCVID=rpAOJeC62x6H5VoupP_hrZ2yDg5MA43TH6f3CjW2Lys30eJ8yCD6EG0P_U8g0KubBR9kogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJIJVCDKtC83fn74MITbbtFbMfIXbR_XKKOLVb6Yfp7keq8CD4cqQx5D3hojapR3QCjRsloDal--S-o2y5jtDTFJblAHQhoALaLJ3xc4Jf7psIJM0PDWbT8U5fKDyhQLaKviaKOjBMb1MMJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe6jQjG8OJT-Hf5r-0nT-5ROMK4OYht5HqR0_hU5K2K62aKDs0JjcBhcqEIL4LfOcKPku5q3UW63PamPL5JK5WbTdVxbSj4Qo3qI4bG-DQU6WbHcZhf8Eal5nhMJFXj7JDMP0-46LKJOy523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0D6JBea_DJ68sb5vfsJTeK4bHHtJYq4b_ePF_e-nZKxtqtjIf256gQP52_PTs3tcUqfDqWb7jJMRnWnchohRjMlnaDp6RDtJmDnkRbfQ405OTaaIO0KJc0R_hHl_RhPJvyTtsXnO7tpOlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVDIyJKLKMIPr5nJbqRkt-fn32-6M-KbtsJOOaCv4ehvOy4oWK441DnPOL-Tt-N8jbU5E3T6IeqvobTrx3M04X-oUbqOBWNFJ0xD5bxQFV6CGQft20b3bMH3m2bLL5I0Oob7jWhk2ep72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ6_8JJPHoKv5b-0_Db5m-tPV-P6H-UnLqbjj0mOZ0l8KttP-OK5Khno20h4JKRCHhx3MJmjC_IOmWIQthpOF3T5d2JJyDMoZqncm3nc4KKJxXMKWeIJo5t5I06FfhUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TF5DjJ-jUK; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=32189_1469_31325_32139_32046_32231_32258_22157; delPer=0; PSINO=7; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PHPSESSID=0a6e7o01jvc3jnq149cbkqa8j5; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1594200791; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1594200791'
    cookiesList = re.findall(r'([\S\s]*?)=([\S\s]*?);', cookies)
    for cookie in cookiesList:
        ck = {'name': cookie[0].strip(), 'value': cookie[1].strip()}
        print(ck)
        browser.add_cookie(ck)  # 添加cookie到浏览器测试对象


def get_content():
    file = open('reply.txt', encoding='utf-8').readlines()  # 读取所有评论
    return choice(file).strip()  # 随机获取一行评论并返回

def reply():
    content = get_content()  # 获取评论内容
    js = "document.getElementById('ueditor_replace').innerHTML='%s'" % content  # 编写js脚本
    browser.execute_script(js)  # 执行js脚本
    browser.find_element_by_css_selector('.poster_submit').click()  # 点击发表按钮

def main():
    # count = 0
    for url in open('/Users/mac/python/tieba/url.txt', encoding='utf-8').readlines():  # 逐行读取url文件
        # count += 1
        # if count >= 5:  # 从url文件中的第5个地址开始回复
        print(url[0])
        browser.get(url)  # 打开地址
        sleep(20)  # 避免回复过快，地址打开后等待10秒钟。
        cookie()  # 添加cookie
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 滚动到页面底部
        reply()  # 写入回复内容并提交
        sleep(30)  # 等待完成提交
        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()  # 关闭网页

if __name__ == '__main__':
    main()