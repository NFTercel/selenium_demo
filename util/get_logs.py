#coding=utf-8

import logging
import os
import datetime

class log():

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志，用于本地调试
        # consle = logging.StreamHandler()
        # self.logger.addHandler(consle)



        # 文件名
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.log'
        log_path = os.path.join(base_dir,'report','logs',file_name)

        # 文件输出文件
        self.file_handle = logging.FileHandler(log_path,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s--> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


    def get_log(self):
        return self.logger


    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()



if __name__ == '__main__':
    user = log()
    loguser = user.get_log()
    loguser.debug('test12567890')
    user.close_handle()








