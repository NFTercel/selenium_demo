#coding=utf-8
import configparser
import os

class ReadIni(object):

    # 构造函数初始化全局变量
    def __init__(self,file=None,node=None):
        if file == None:
            file = os.path.abspath('./local_element.ini')
        if node == None:
            self.node = "ReginsterElement"
        else:
            self.node = node

        self.cf = self.load_ini(file)

    ########## 需要重构
    def get_file(self,file):
        # 文件：'./local_element.ini'
        file = os.path.abspath(file)

    #读取文件
    def load_ini(self,file):
        cf = configparser.ConfigParser()
        cf.read(file)
        return cf

    # #获取数据
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data



if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value("user_name"))