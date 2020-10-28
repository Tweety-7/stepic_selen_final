from .base_page import BasePage
from pages.locators import ProductPageLocators
class PageObject(BasePage):
	def add_in_basket(self):

	def should_be_in_basket(self):
		assert