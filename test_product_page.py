import pytest
from pages.product_page import PageObject
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

link_207 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_2019 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_95 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

# @pytest.mark.xfail
@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
	link = link_2019
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
	time.sleep(10)
	page.add_is_ok(name, price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = link_207
	page =  PageObject(browser, link)
	# Открываем страницу товара
	page.open()
	# Добавляем товар в корзину 
	page.click_to_add()	
	# !!! Проверяем, что нет сообщения об успехе с помощью is_not_element_present / сообщение есть = фолс
	page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	link = link_95
	page = PageObject(browser, link)
	page.open()
	page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = link_95
	page = PageObject(browser, link)
	page.open()
	page.go_to_login_page()
@pytest.mark.need_review	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	# Гость открывает страницу товара
	link = link_207
	page = PageObject(browser, link)
	page.open()
	# Переходит в корзину по кнопке в шапке
	basket_page = page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	# Ожидаем, что в корзине нет товаров
	basket_page.should_be_basket_is_empty()
	# Ожидаем, что есть текст о том что корзина пуста 
	basket_page.basket_text_empty()
@pytest.mark.user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = link_login
		login_page = LoginPage(browser, link)
		login_page.open()
		user_fake = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(user_fake,"1234qwert")
		login_page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = link_2019
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

# @pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
	link = link_207
	# Открываем страницу товара
	page =  PageObject(browser, link)
	page.open()
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = link_207
	page =  PageObject(browser, link)
	page.open()	
	# 	# Добавляем товар в корзину
	page.click_to_add()
	# 	# Проверяем, что нет сообщения об успехе с помощь is_disappeared (элемент не исчезнет)
	# тру, если эл-т исчезнет или не было. Эл-т есть и не исчезает = фолс
	page.should_not_be_success_message()


	def test_user_cant_see_success_message(self, browser):
		link = link_207
		page =  PageObject(browser, link)
		page.open()
		# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
		page.should_not_be_success_message()
		
