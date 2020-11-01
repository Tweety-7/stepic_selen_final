# from base_page import BasePage
# from .base_page.py import BasePage
# .pages.main_page import MainPage
# from pages.main_page import MainPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self,browser):
        	link = "http://selenium1py.pythonanywhere.com/"
        	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        	page = MainPage(browser, link)
        	page.open()
        	page.should_be_login_link()
    def test_guest_can_go_to_login_page(self,browser):
            link = "http://selenium1py.pythonanywhere.com/"
        	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
            page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open()                      # открываем страницу
            login_page = page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_login_page_its_ok(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


'''
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/ru"
    page = MainPage(browser, link)
    page.open()
    # page.should_be_basket_link()
    basket_page = page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_is_empty()
    # Ожидаем, что есть текст о том что корзина пуста 
    basket_page.basket_text_empty()
'''


