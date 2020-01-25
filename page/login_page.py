#coding=utf-8
from common.find_element import Find_Element

class LoginPage(object):
    def __init__(self,driver):
        self.fd = Find_Element(driver)

    def get_username_elememnt(self):
        return self.fd.get_element("user_name")

    def get_password_elememnt(self):
        return self.fd.get_element("passwd")

    def get_user_private_elememnt(self):
        return self.fd.get_element("user_private")

    def get_submit_elememnt(self):
        return self.fd.get_element("submit")

    def get_err_message(self):
        return self.fd.get_element('pwandname_err_mess')

    def get_empty_message(self):
        return self.fd.get_element('pwname_empty')