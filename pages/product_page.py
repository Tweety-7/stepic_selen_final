from .base_page import BasePage
from pages.locators import ProductPageLocators
import time

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

class PageObject(BasePage):

	# def add_in_basket(self):
		# self.shoud_be_btn()
		# self.should_be_alert()
		# self.should_be_in_basket()
		def click_to_add(self):
			btn_add = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
			btn_add.click()
		def shoud_be_btn(self):
			assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "ADD_BASKET is absent"
		def add_is_ok(self,name, price):
			name_after_add = self.browser.find_element_by_class_name("alert.alert-safe.alert-noicon.alert-success.fade.in")
			# time.sleep(3)
			price_in_basket = self.browser.find_element_by_xpath('//*[@id="messages"]/div[3]/div/p[1]/strong')
			# print("ТМЯ2 = ", name_after_add.text)
			# print("ЦЕНА = ", price_in_basket.text)
			# time.sleep(3)
			# name_after_add = self.browser.find_element_by_class_name("alertinner ")
			# alert = self.browser.switch_to.alert
			# name_after_add = alert.text
			# print("PRICE2=",price)
			# print("NAME2=",name.split("\n")[0])
			# print("NAME3=", name_after_add.text.split("has been added")[0])
			assert name.split("\n")[0] in name_after_add.text, "name not add in basket"
			assert price in price_in_basket.text, "price_in_basket not ok"
		# def should_be_alert(self):
		# btn = self.is_element_present(*ProductPageLocators.ADD_BASKET)
		# btn.click() 
			# WebDriverWait(self.browser, 3).until(EC.alert_is_present())
			# mb_al = self.browser.switch_to_alert
			# mb_al=self.browser.find_element_by_id("input_value")
			# print(mb_al)
			# alert_text = mb_al['alert'].get('text')
			# alert_text, "не алерт всплывает"
			# print(mb_al.split('=')[1:3])
			



	# def should_be_in_basket(self):
	# 	assert True , "not in basket"