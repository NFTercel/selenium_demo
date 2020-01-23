#coding=utf-8
from selenium import webdriver
import time
import random
import string
from PIL import Image
import pytesseract

driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("https://gitee.com/login")
    driver.maximize_window()
    time.sleep(5)

def driver_quit():
    driver.close()
    driver.quit()

# 获取element的信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element


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


#h获取字符串,type(d:数字，low:小写字母，upper：大写字母，l:大小写字母，dl:数字字母，dlp:数字字母特殊字符)，num（位数）,count:个数默认为1
def get_random_str(type,num,count=None):
    data = ''
    strarr = []
    if count == None:
        count = 1

    if type == "d":
        data = string.digits
    elif type == "low":
        data = string.ascii_lowercase
    elif type == "upper":
        data = string.ascii_uppercase
    elif type == "l":
        data == string.ascii_letters
    elif type == "dl":
        data = string.digits + string.ascii_letters
    elif type == "dlp":
        data = string.digits + string.ascii_letters + string.punctuation
    print('data: ',data)
    print('count: ',count)
    print('num: ',num)
    for i in range(count):
        str = random.sample(data, num)
        strarr.append(''.join(str))
    print("string list: ",strarr)
    return strarr







##############保存图片(！获取元素的方法设计******)
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

# 模式显示时间格式，输入任意参数可用于保存文件的时间格式
def get_time(type=None):
    if type == None:
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    else:
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    print('Time: ',nowtime)
    return nowtime


def run_main():
    driver_init()
    get_element("user_login").send_keys("selenium_training")
    get_element("user_password").send_keys("test123456")
    driver.find_element_by_css_selector(
        "#new_user > div.session-login__body > div > div > div.two.fields > div:nth-child(1) > div").click()
    driver.find_element_by_name("commit").click()
    time.sleep(5)
    driver_quit()

run_main()