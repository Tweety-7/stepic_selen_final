import pytest
from pages.product_page import PageObject
from pages.locators import ProductPageLocators

	# @pytest.mark.parametrize(promo_code, range(10))
# 	@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='')) for i in range(10)])
@pytest.mark.xfail
@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
	# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
	page = PageObject(browser, link)
	page.open()
	page.shoud_be_btn()
	name = browser.find_element(*ProductPageLocators.NAME_BOOK)
	price = browser.find_element(*ProductPageLocators.PRICE_BOOK)
	name = name.text
	price = price.text
	page.click_to_add()
	page.solve_quiz_and_get_code()
	page.add_is_ok(name, price)
