
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL = (By.ID, "id_registration-email")
	PASSWORD = (By.ID, "id_registration-password1")
	PASSWORD_2 = (By.ID, "id_registration-password2")
	BTN_REG = (By.CSS_SELECTOR, '#register_form > button')
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
	BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	# EMPTY_BASKET = (By.XPATH, "//*[@id="content_inner"]/p/text()") //*[@id="default"]/div[2]/div/div[3]
	# EMPTY_BASKET = (By.id, "content_inner")
class BasketPageLocators():
	BASKET_TEXT = (By.ID, "content_inner")
	PRODUCTS_IN_BASKET = (By.CLASS_NAME, "table table-condensed")