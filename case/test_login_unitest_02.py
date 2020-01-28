# coding=utf-8
import sys
import time

sys.path.append('/Users/liliang/PycharmProjects/selenium-train/')
from business.login_business import LoginBusiness

from selenium import webdriver

import unittest

# 1. webDriver.Close() - Close the browser window that the driver has focus of //关闭当前焦点所在的窗口
# 2. webDriver.Quit() - Calls dispose //调用dispose方法
# 3. webDriver.Dispose() Closes all browser windows and safely ends the session 关闭所有窗口，并且安全关闭session


class FirstCase(unittest.TestCase):
    '''每条case前执行'''

    def setUp(self):
        print('前置条件')

    def tearDown(self):
        print('后置条件')
    @unittest.skip('跳过执行')
    def testfirst003(self):
        print('第一条case')

    def testfirst004(self):
        print('第二条case')

    #装饰器@classmethod，执行所有用例
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

'''
结果：
前置条件
第一条case
后置条件
.前置条件
第二条case
后置条件

执行顺序控制根据：测试方法名如：test_**001、test_**002...,方法二：通过TestSuite添加执行顺序

'''

if __name__ == '__main__':
    # unittest.main()#执行所用测试用例
    #定制测试用例
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('testfirst001'))
    suite.addTest(FirstCase('testfirst002'))
    unittest.TextTestRunner().run(suite)

'''
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gitee.com/login')
        self.login_b = LoginBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_emp(self):
        result = self.login_b.login_name_error('123', '')
        if result == True:
            print('用例执行成功，登录失败')

    def test_login_name_err(self):
        result = self.login_b.login_name_error('1234', '1234567')
        if result == True:
            print('用例执行成功，登录失败')

    def test_login_password_err(self):
        result = self.login_b.login_name_error('selenium_training', '123')
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


# if __name__ == '__main__':
#     unittest.main()
'''