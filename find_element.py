#coding=utf-8

from util.read_ini import ReadIni

class Find_Element():

    #下面需要用到driver，所以这里进行传参
    def __init__(self,driver):
        self.driver = driver

    #获取单个元素
    def get_element(self,key,*args):
        #key 未local_element.ini中等号前面的部分，如：user_name=id>"user_login" key为：user_name
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        data = data.split(">",1)
        by = data[0]
        value = data[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_name(value)
        elif by == "linktext":
            return  self.driver.find_element_by_link_text(value)
        elif by == "partiallinxtext":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == 'tagname':
            return self.driver.find_element_by_tag_name(value)
        elif by == "classname":
            return  self.driver.find_element_by_class_name(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == 'jsscript':
            return self.driver.execute_script(value,*args)
        elif by == "jsasyncscript":
            return  self.driver.execute_async_script(value,*args)

    # 获取多个元素
    def get_elements(self,key,*args):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        data = data.split(">", 1)
        by = data[0]
        value = data[1]
        by = data[0]
        value = data[1]
        if by == 'id':
            return self.driver.find_elements_by_id(value)
        elif by == 'name':
            return self.driver.find_elements_by_name(value)
        elif by == "linktext":
            return  self.driver.find_elements_by_link_text(value)
        elif by == "partiallinxtext":
            return self.driver.find_elements_by_partial_link_text(value)
        elif by == 'tagname':
            return self.driver.find_elements_by_tag_name(value)
        elif by == "classname":
            return  self.driver.find_elements_by_class_name(value)
        elif by == "css":
            return self.driver.find_elements_by_css_selector(value)
        elif by == "xpath":
            return self.driver.find_elements_by_xpath(value)
        elif by == 'jsscript':
            return self.driver.execute_script(value,*args)
        elif by == "jsasyncscript":
            return  self.driver.execute_async_script(value,*args)




# if __name__ == '__main__':
#     fl = Find_Element()
#     fl.get_element("user_name")