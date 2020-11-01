import pytest
from pages.product_page import PageObject
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.basket_page import BasketPage
import time
	# @pytest.mark.parametrize(promo_code, range(10))
# 	@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='')) for i in range(10)])
# @pytest.mark.xfail
# @pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6", "7", "8", "9"])
# def test_guest_can_add_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# 	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# 	    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
# 	# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
# 	page = PageObject(browser, link)
# 	page.open()
# 	page.shoud_be_btn()
# 	name = browser.find_element(*ProductPageLocators.NAME_BOOK)
# 	price = browser.find_element(*ProductPageLocators.PRICE_BOOK)
# 	name = name.text
# 	price = price.text
# 	page.click_to_add()
# 	page.solve_quiz_and_get_code()
# 	page.add_is_ok(name, price)
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 	page =  PageObject(browser, link)
# 	# Открываем страницу товара
# 	page.open()
# 	# Добавляем товар в корзину 
# 	page.click_to_add()	
# 	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
# 	assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
# def test_guest_cant_see_success_message(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 	# Открываем страницу товара
# 	page =  PageObject(browser, link)
# 	page.open()
# 	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
# 	assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 		# Открываем страницу товара
# 	page =  PageObject(browser, link)
# 	page.open()	
# 	# 	# Добавляем товар в корзину
# 	page.click_to_add()
# 	# 	# Проверяем, что нет сообщения об успехе с помощь is_disappeared (элемент не исчезнет)
# 	assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
# def test_guest_should_see_login_link_on_product_page(browser):
# 	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
# 	page = PageObject(browser, link)
# 	page.open()
# 	page.should_be_login_link()
# # @pytest.mark.xfail
# def test_guest_can_go_to_login_page_from_product_page(browser):
# 	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
# 	page = PageObject(browser, link)
# 	page.open()
# 	page.go_to_login_page()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	# Гость открывает страницу товара
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject(browser, link)
	page.open()
	# Переходит в корзину по кнопке в шапке
	basket_page = page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	time.sleep(40)
	# Ожидаем, что в корзине нет товаров
	basket_page.should_be_basket_is_empty()
	# Ожидаем, что есть текст о том что корзина пуста 
	basket_page.basket_text_empty()