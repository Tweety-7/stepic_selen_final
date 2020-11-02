from .base_page import BasePage
import time
from pages.locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert  self.browser.current_url, "not correct login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login_form absent"
    def should_be_register_form(self):
            # реализуйте проверку, что есть форма регистрации на странице
            assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register_form absent"
    def register_new_user(self, email, password):
        # should_be_register_form()
        em = self.browser.find_element(*LoginPageLocators.EMAIL)    
        em.send_keys(email)
        pas = self.browser.find_element(*LoginPageLocators.PASSWORD)
        pas.send_keys(password)
        pas2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        pas2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn.click()
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

