#coding=utf-8
from handle.login_handle import LoginHandle
import time
class LoginBusiness:
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)

    def base_action(self,username,password):
        print('************base_action***********')
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.click_user_private()
        self.login_h.click_submit()
        time.sleep(15)

    # 用户名错误
    def login_name_error(self,username,password):
        print("**************business*****************")
        self.base_action(username,password)
        if self.login_h.get_error_message('name_error','帐号或者密码错误'):
            print('验证：用户名错误登录不成功')
            return True
        else:
            return False
        time.sleep(5)

    # 密码错误
    def login_password_error(self,username,password):
        self.base_action(username, password)
        if self.login_h.get_error_message('name_error','帐号或者密码错误'):
            print('验证：密码错误登录不成功')
            return True
        else:
            return False

    #用户名密码为空
    def login_empty(self,username,password):
        self.base_action(username, password)
        if self.login_h.get_error_message('name_error','用户名为必填项'):
            print('验证：用户名、密码为必填项')
            return True
        else:
            return False


    def login_success(self,username,password):
        self.base_action(username, password)


