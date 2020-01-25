#coding=utf-8
from page.login_page import LoginPage
class LoginHandle(object):

    def __init__(self,driver):
        self.login_p = LoginPage(driver)

    '''用户名'''
    def send_username(self,username):
        self.login_p.get_username_elememnt().send_keys(username)

    '''密码'''
    def send_password(self,passwd):
        self.login_p.get_password_elememnt().send_keys(passwd)

    '''隐私协议'''
    def click_user_private(self):
        self.login_p.get_user_private_elememnt().click()

    '''登录'''
    def click_submit(self):
        self.login_p.get_submit_elememnt().click()

    # '''用户名或密码错误提示'''
    # def get_err_message(self):
    #     self.login_p.get_err_message().text
    #
    # '''用户名密码为空的提示'''
    # def get_empty_message(self):
    #     self.login_p.get_empty_message().text
    '''获取错误信息'''
    def get_error_message(self,info,message):
        if info == 'name_error' or info == 'pw_error':
            text = self.login_p.get_err_message().text
        elif info == 'empty':
            text = self.login_p.get_empty_message().text
        return text

















