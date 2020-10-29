from pages.product_page import PageObject
import time

def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	# btn = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
	page = PageObject(browser, link)
	page.open()
	page.shoud_be_btn()
	name = browser.find_element_by_class_name("col-sm-6.product_main")
	price = browser.find_element_by_class_name("price_color")
	name = name.text
	price = price.text
	# print("ИМЯ",name)
	# print("PRICE = ", price)
	# page.click_to_add()
	page.click_to_add()
	page.solve_quiz_and_get_code()
	page.add_is_ok(name, price)
# btn btn-lg btn-primary btn-add-to-basket