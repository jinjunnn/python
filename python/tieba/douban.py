# 贴吧自动回帖
from selenium import webdriver
import time
from random import choice
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.douban.com/')
time.sleep(20)


def get_content():
    file = open('reply.txt', encoding='utf-8').readlines()  # 读取所有评论
    return choice(file).strip()  # 随机获取一行评论并返回


def get_url():
    file = open('douban_url'.txt', encoding='utf-8').readlines()  # 读取所有评论
    return choice(file).strip()  # 随机获取一行评论并返回


#   创建一个帖子
def create_post(url, title, content):
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_name("title").send_keys(title)
    time.sleep(10)
    driver.find_element_by_id("ueditor_replace").send_keys(content)
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()


#创建一个帖子
# u = 'https://tieba.baidu.com/f?kw=代购&fr=index'
# create_post(u,'我就是来发一个帖子的','今天的消息怎么样呀。')


def reply_post(url, content):
    driver.get(url)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#滚动到页面底部
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="last"]').send_keys(content)#找到输入框
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[4]/form/span[1]/input').click()
    time.sleep(30)
    return


def cycle_reply_post():
    for item in range(0, 10000):
        content = get_content()
        urls = get_url()
        reply_post(urls, content)


cycle_reply_post()
