#coding=utf-8
import  sys
import time
sys.path.append('/Users/liliang/PycharmProjects/selenium-train/')
from business.login_business import LoginBusiness

from selenium import webdriver

class LoginCase(object):

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('https://gitee.com/login')
        self.login_b =LoginBusiness(driver)

    def test_login_emp(self):
        result = self.login_b.login_name_error('123','')
        if result == True:
            print('用例执行成功，登录失败')

    def login_name_err(self):
        result = self.login_b.login_name_error('1234','1234567')
        if result == True:
            print('用例执行成功，登录失败')


    def login_password_err(self):
        result = self.login_b.login_name_error('selenium_training','123')
        print('***********login_password************')
        if result == True:
            print('用例执行成功，登录失败')



    def test_login_succ(self):
        self.login_b.login_success('selenium_training', 'test123456')

def main():
    first = LoginCase()
    # first.test_login_succ()
    first.login_name_err()
    # first.login_password_error()
    # first.test_login_empty()




if __name__ == '__main__':
    main()