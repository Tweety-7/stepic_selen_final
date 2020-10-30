# class LoginPageLocators(B)
# 	def __init__(self):
# 		pass
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
	ADD_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
	ALERT_NAME = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')
	PTICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
	NAME_BOOK = (By.CLASS_NAME, "col-sm-6.product_main")
	PRICE_BOOK = (By.CLASS_NAME, "price_color")
	SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in")
class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")