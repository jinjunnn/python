# 贴吧自动回帖
from selenium import webdriver
import threading
import re,time
from random import choice
from selenium.common.exceptions import NoSuchElementException  #导入NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_file_douban = '/Users/mac/python/tieba/douban_url.txt'
url_file_tieba = '/Users/mac/python/tieba/url.txt'

driver1 = webdriver.Chrome()
driver1.maximize_window()



str_cookie = 'AA5BF47A3D5BE5D08A499830AD87F592; PSTM=1584003278; BAIDUID=AA5BF47A3D5BE5D0BDA752A2CCFD55B8:FG=1; H_WISE_SIDS=139913_143435_143879_144427_141744_144134_141901_142780_144482_144897_131861_131247_137745_144741_138883_141942_127969_140065_144337_140593_143060_141808_144607_141008_143471_144727_143923_131423_144289_128700_142207_144219_144004_107312_138596_139910_144105_143477_142426_142911_143548_144239_142113_143855_144098_140843_110085; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=JYUX5hcmcwSE1BZGZzS2pzczFoV0NkdGtEaHkyVGF5dW5HRTVTN0dydjZiRE5mRVFBQUFBJCQAAAAAAAAAAAEAAAAmChd9vvbVvca9sLK-qcPr1LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPrfC1~63wtfSj; delPer=0; PSINO=6; H_PS_PSSID=32189_1469_31325_32139_32046_32231_32258_22157'  #cookie字符串用f12查看网络中的请求贴吧的，请求头中的cookie
lists=re.findall('([\s\S]*?)=([\s\S]*?); ',str_cookie+'; ')
for  l in lists:
    ck={'name':l[0],'value':l[1]}
    print(ck)
    driver1.add_cookie(ck)           #来个正则把cookie字符串转成slenium的cookie格式字典，添加到driver。cookie字符串是请求贴吧时用f12查看的 network的headers的请求头的cookie，复制就可以了，这样selenium也可以免登陆
driver1.get('https://tieba.baidu.com/p/4778694923')










# driver1 = webdriver.Chrome()
# driver1.maximize_window()
# driver1.get('https://passport.baidu.com/v2/?login')
# time.sleep(20)

# driver2 = webdriver.Chrome()
# driver2.maximize_window()
# driver2.get('https://passport.baidu.com/v2/?login')
# time.sleep(10)

# driver3 = webdriver.Chrome()
# driver3.maximize_window()
# driver3.get('https://passport.baidu.com/v2/?login')
# time.sleep(10)


def get_content():
    file = open('reply.txt', encoding='utf-8').readlines()  # 读取所有评论
    return choice(file).strip()  # 随机获取一行评论并返回

def get_url(u):
    file = open(u, encoding='utf-8').readlines()  # 读取所有评论
    return choice(file).strip()  # 随机获取一行评论并返回

#   创建一个帖子
def create_post(url,title,content):
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_name("title").send_keys(title)
    time.sleep(10)
    driver.find_element_by_id("ueditor_replace").send_keys(content)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()


def find_element(browser):
    while True:
        try:
            print('try')
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")#滚动到页面底部
            browser.find_element_by_xpath(
                '//*[@id="ueditor_replace"]').send_keys(get_content())  #找到输入框

        except Exception as e:
            print("查找输入框失败", format(e))
            time.sleep(2)

        else:
            print('找到输入框')
            try:
                browser.find_element_by_xpath(
                    '//*[@id="ueditor_replace"]').send_keys(
                        get_content())  #找到输入框
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[3]/div/a').click()
                print('顶帖成功')
                time.sleep(90)
                return

            except Exception as e:
                print("顶帖失败", format(e))
                return


def map_pages(browser,page_links):
    lists = open(page_links, encoding='utf-8').readlines()
    for i in range(200):
        for index, value in enumerate(lists):  # 逐行读取url文件
            browser.switch_to_window(browser.window_handles[index])
            time.sleep(2)
            find_element(browser)



def page_list(browser,page_links, thread_name):
    lists = open(page_links, encoding='utf-8').readlines()
    for index, value in enumerate(lists):  # 逐行读取url文件
        browser.execute_script('window.open("{}")'.format(
            value.replace('\n', '')))
        time.sleep(2)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")#滚动到页面底部
        time.sleep(2)
    browser.switch_to_window(browser.window_handles[0])
    browser.close()
    map_pages(browser,page_links)

def main():
    t1 = threading.Thread(
        target=page_list, args=(driver1, url_file_tieba, '一'))
    t2 = threading.Thread(
        target=page_list, args=(driver2, url_file_tieba,'二'))
    t3 = threading.Thread(
        target=page_list,args=(driver3, url_file_tieba, '三'))
    # t4 = threading.Thread(target=post, args=(url_file_douban,driver1, reply_post_douban,'四'))
    # t5 = threading.Thread(target=post, args=(url_file_douban,driver2, reply_post_douban,'五'))
    # t6 = threading.Thread(target=post, args=(url_file_douban,driver3, reply_post_douban,'六'))
    t1.start()
    time.sleep(30)
    t2.start()
    time.sleep(30)
    t3.start()
    # t4.start()
    # t4.join()
    # t5.start()
    # t5.join()
    # t6.start()
    # t6.join()

# main()