#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
import string
from itertools import product
from PIL import Image
import pytesseract

# 参考：https://www.cnblogs.com/tobecrazy/p/4570494.html
driver = webdriver.Chrome()

driver.get("https://gitee.com/login")
driver.maximize_window()
time.sleep(5)

# 基础方法

#获取邮箱方法:namenum(邮箱名字的位数)，mailcount(邮箱的个数)
def make_email(namenum,mailcount=None):
    if mailcount == None:
        mailcount = 1
    email = []
    data = string.ascii_letters+string.digits #字母和数字,特殊字符 string.ascii_lowercase、string.punctuation、string.ascii_uppercase
    for i in range(mailcount):
        email_type = random.choice(('@163.com', '@qq.com', '@sina.com', '@126.com'))
        data = random.sample(data, namenum)
        email_start = ''.join(data)
        email.append(email_start+email_type)
    print('Email: ', email)
    return email

# 模式显示时间格式，输入任意参数可用于保存文件的时间格式
def get_time(type=None):
    if type == None:
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    else:
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    print('Time: ',nowtime)
    return nowtime



#保存图片
def make_qr(elment,filename=None):
    driver.save_screenshot(filename)
    image_elment = driver.find_element_by_name(elment)
    #获得图片的尺寸
    left = image_elment.location['x']
    top = image_elment.location['y']
    right = image_elment.size['width']+left
    height = image_elment.size['height']+top
    #裁剪图片
    im = Image.open(filename)
    img = im.crop(left,top,right,height)
    img.save(filename)

#识别规则图片
def identify_normal_img(filename):
    img = Image.open(filename)
    text = pytesseract.image_to_string(img)
    return text

#识别非规则图片（使用三方付费api，可以自己研究算法实现）
# # https://www.showapi.com/apiGateway/view/?apiCode=1754&pointCode=2
# def identify_unnormal_img(filename):
#     from ShowapiRequest import ShowapiRequest
#     r = ShowapiRequest("http://route.showapi.com/1754-2", "my_appId", "my_appSecret")
#     r.addBodyPara("image", "")
#     r.addBodyPara("with_face", "1")
#     res = r.post()
#     res.json()[]['showapi_res_body']['Resuit']
#     print(res.text)  # 返回信息


# 判断元素是否存在(等待加载完成后查找)
'''
# element = driver.find_element_by_id("")
locator = (By.CLASS_NAME,"element")
WebDriverWait(driver,1).until(EC.invisibility_of_element_located(locator))
'''
name = driver.find_element_by_id("user_login").send_keys('selenium_training')

#获取元素的属性的方法get_attribute，填入获取的属性名
pw = driver.find_element_by_id("user_password")
text = pw.get_attribute("placeholder")
print(text)
pw.send_keys("test123456")
# 获取输入的信息内容
print(pw.get_attribute("value"))

driver.find_element_by_css_selector("#new_user > div.session-login__body > div > div > div.two.fields > div:nth-child(1) > div").click()
driver.find_element_by_name("commit").click()




driver.close()
driver.quit()

