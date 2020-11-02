from pages.locators import BasketPageLocators
from pages.base_page import BasePage

		# В классе BasePage реализуйте
		# соответствующий метод для перехода 
		# в корзину. Создайте файл basket_page.py 
		# и в нем класс BasketPage. Реализуйте там необходимые проверки,
		#  в том числе отрицательную, которую мы обсуждали в предыдущих шагах.
class BasketPage(BasePage):

	def should_be_basket_url(self):
			assert self.browser.current_url, "not correct basket url"
	def basket_text_empty(self):
		text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
		assert "Ваша корзина пуста" or "Your basket is empty" in text_in_basket.text, "корзина не пустая"
	#ожидаем пустую корзину
	def should_be_basket_is_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "should not be product in basket"

