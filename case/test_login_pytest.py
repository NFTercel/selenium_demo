#coding=utf-8
import  sys
import time
sys.path.append('/Users/liliang/PycharmProjects/selenium-train/')
from business.login_business import LoginBusiness

from selenium import webdriver
import pytest

'''
class Test_pytest():
    # 每条case前执行
    def setup(self):
        print('执行前')

    def teardown(self):
        print('执行后')

    def testfirst001(self):
        print('第一条case')

    def testfirst002(self):
        print('第二条case')
'''

# if __name__ == '__main__':
#     pytest.main(['-s','/Users/liliang/PycharmProjects/selenium-train/case/test_login_pytest.py'])

'''
pytest:不支持类间调用关系（__init__）,可以使用contest.py实现功能
'''

class Test_LoginCase(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gitee.com/login')
        self.login_b =LoginBusiness(self.driver)

    def teardown(self):
        self.driver.close()

    def _test_login_emp(self):
        result = self.login_b.login_name_error('123','')
        if result == True:
            print('用例执行成功，登录失败')

    def _test_login_name_err(self):
        result = self.login_b.login_name_error('1234','1234567')
        if result == True:
            print('用例执行成功，登录失败')


    def _test_login_password_err(self):
        result = self.login_b.login_name_error('selenium_training','123')
        print('***********login_password************')
        if result == True:
            print('用例执行成功，登录失败')



    def test_login_succ(self):
        self.login_b.login_success('selenium_training', 'test123456')

# def main():
#     first = LoginCase()
#     # first.test_login_succ()
#     first.login_name_err()
#     # first.login_password_error()
#     # first.test_login_empty()




if __name__ == '__main__':
    pytest.main(['-s','/Users/liliang/PycharmProjects/selenium-train/case/test_login_pytest.py'])
