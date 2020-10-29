from pages.product_page import PageObject

def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	# btn = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
	page = PageObject(browser, link)
	page.open()
	# page.shoud_be_btn()
	# page.click_to_add()
	page.click_to_add()
	page.solve_quiz_and_get_code()
# btn btn-lg btn-primary btn-add-to-basket