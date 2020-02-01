# coding=utf-8
import sys
import time
import os
sys.path.append('/Users/liliang/PycharmProjects/selenium-train/')
from business.login_business import LoginBusiness

from selenium import webdriver

import unittest
from report.tools import HTMLTestRunner
import ddt
from util.excel_util import ExcelUtil
from util.get_logs import log

ex = ExcelUtil()
data = ex.get_data()


# 1. webDriver.Close() - Close the browser window that the driver has focus of //关闭当前焦点所在的窗口
# 2. webDriver.Quit() - Calls dispose //调用dispose方法
# 3. webDriver.Dispose() Closes all browser windows and safely ends the session 关闭所有窗口，并且安全关闭session


# class FirstCase(unittest.TestCase):
#     '''每条case前执行'''
#
#     def setUp(self):
#         print('前置条件')
#
#     def tearDown(self):
#         print('后置条件')
#
#
#     @unittest.skip('跳过执行')
#     def testfirst001(self):
#         print('第一条case')
#
#     def testfirst002(self):
#         print('第二条case')
#
#     #装饰器@classmethod，执行所有用例
#     @classmethod
#     def setUpClass(cls):
#         print('所有case执行之前前置')
#
#     @classmethod
#     def tearDownClass(cls):
#         print('所有case执行之后的后置')

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

# if __name__ == '__main__':
#     # unittest.main()#执行所用测试用例
#     #定制测试用例
#     report_file = os.path.join(os.getcwd(),'report/report.html')
#     file = open(report_file,'wb')
#
#     suite = unittest.TestSuite()
#     suite.addTest(FirstCase('testfirst001'))
#     suite.addTest(FirstCase('testfirst002'))
#     # unittest.TextTestRunner().run(suite)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='This is the Report',
#                                   description=u'测试报告',verbosity=2)
#     runner.run(suite)



@ddt.ddt
class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = log()
        cls.log_config = cls.logger.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gitee.com/login')
        self.log_config.debug('创建driver')
        self.login_b = LoginBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in  self._outcome.errors :
            print('method_name: ',method_name,'error：',error)

            if error:
                case_name = self._testMethodName
                img_name = os.path.join(os.getcwd()+'/report/screenshot/'+case_name+'.png')
                print('img_name: ',img_name)
                self.driver.get_screenshot_as_file(img_name)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.logger.close_handle()



    # @ddt.data(
    #     ['liliang','dfghjk','name_error','用户名为必填项'],
    #     ['liliang','dfghjk','name_error','用户名为必填项'],
    #     ['liliang', 'dfghjk', 'name_error', '用户名为必填项'],
    # )
    #
    # @ddt.unpack
    # def test_login_emp(self,username,password,assertkey,asserttext):
    #     result = self.login_b.login_function(username, password,assertkey,asserttext)
    #     self.assertFalse(result)

    @ddt.data(*data)
    def test_login_emp(self,data):
        username, password, assertkey, asserttext = data
        result = self.login_b.login_function(username, password,assertkey,asserttext)
        self.assertFalse(result)


    # def _test_login_name_err(self):
    #     result = self.login_b.login_name_error('1234', '1234567')
    #     self.assertFalse(result)
    #
    # def test_login_password_err(self):
    #     result = self.login_b.login_name_error('selenium_training', '123')
    #     self.assertFalse(result)
    #
    # def test_login_succ(self):
    #     succ = self.login_b.login_success('selenium_training', 'test123456')
    #     self.assertTrue(succ)



# def main():
#     first = LoginCase()
#     # first.test_login_succ()
#     first.login_name_err()
#     # first.login_password_error()
#     # first.test_login_empty()


if __name__ == '__main__':
    unittest.main()
