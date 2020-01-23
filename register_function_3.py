#coding=utf-8
from selenium import webdriver
import time
import random
import string
from PIL import Image
import pytesseract
from find_element import Find_Element
class RegisterFunction(object):
    '''将获取控件的方法封装到find_element.py中'''

    #初始化driver,支持多浏览器i
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    #获取driver并打开url
    def get_driver(self,url,i=None):
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        elif i == 2:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    #获取用户信息，获取element，driver传入find_element,key为ini等号前内容
    def get_user_element(self,key):
        #将driver传给find_element
        find_element = Find_Element(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    #输入用户信息
    def send_element(self,key,data):
        self.get_user_element(key).send_keys(data)

    #随机文件
    def make_email(namenum, mailcount=None):
        if mailcount == None:
            mailcount = 1
        email = []
        data = string.ascii_letters + string.digits  # 字母和数字,特殊字符 string.ascii_lowercase、string.punctuation、string.ascii_uppercase
        for i in range(mailcount):
            email_type = random.choice(('@163.com', '@qq.com', '@sina.com', '@126.com'))
            data = random.sample(data, namenum)
            email_start = ''.join(data)
            email.append(email_start + email_type)
        print('Email: ', email)
        return email

    #保存图片
    def make_qr(key, filename=None):
        self.driver.save_screenshot(filename)
        image_elment = self.get_user_element(key)
        # 获得图片的尺寸
        left = image_elment.location['x']
        top = image_elment.location['y']
        right = image_elment.size['width'] + left
        height = image_elment.size['height'] + top
        # 裁剪图片
        im = Image.open(filename)
        img = im.crop(left, top, right, height)
        img.save(filename)


    def main(self):
        self.send_element('user_name','selenium_training')
        self.send_element('passwd','test123456')
        self.get_user_element('user_private').click()
        self.get_user_element('submit').click()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('https://gitee.com/login',i)
        register_function.main()
