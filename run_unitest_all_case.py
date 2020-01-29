# coding=utf-8
import unittest
from report.tools import HTMLTestRunner
import os


'''
使用方法一：
http://tungwaiyip.info/software/HTMLTestRunner.html
https://github.com/findyou/HTMLTestRunnerCN
HtmlTestRunner工具直接引入到：report/tools
导入方法：from report.tools import HTMLTestRunner

使用方法二：
sudo cp ~/Desktop/HtmlTestRunner.py /Library/Frameworks/Python.framework/Versions/3.7/lib

'''

class RunCase(unittest.TestCase):


    def test_case01(self):
        report_file = os.path.join(os.getcwd(), 'report/report.html')
        file = open(report_file, 'wb')
        case_path = os.path.join(os.getcwd(), 'case')
        print('case_path: ', case_path)
        # unittest.TextTestRunner().run(suite) #直接执行测试
        # suite = unittest.defaultTestLoader.discover(case_path, 'test_*')  #执行所有已test开头的文件
        suite = unittest.defaultTestLoader.discover(case_path, 'test_login_unitest_ddt.py') #执行指定测试类


        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='This is the Report',
                                               description=u'测试报告', verbosity=2)
        runner.run(suite)



if __name__ == '__main__':
    unittest.main()
