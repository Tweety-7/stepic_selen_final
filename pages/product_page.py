from .base_page import BasePage
from pages.locators import ProductPageLocators
import time

class PageObject(BasePage):
		def click_to_add(self):
			btn_add = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
			btn_add.click()
		def shoud_be_btn(self):
			assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "ADD_BASKET is absent"
		def add_is_ok(self,name, price):
			name_after_add = self.browser.find_element(*ProductPageLocators.ALERT_NAME)
			price_in_basket = self.browser.find_element(*ProductPageLocators.PTICE_IN_BASKET)
			assert name.split("\n")[0] == name_after_add.text.split("has been added")[0][2:-1], "name not add in basket"
			assert price == price_in_basket.text, "price_in_basket not ok"
		def should_not_be_success_message(self):
			assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "should not be succses"