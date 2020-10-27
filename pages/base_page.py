from selenium.common.exceptions import NoSuchElementException
class  BasePage(object):
	"""docstring for  BacePage"""
	# конструктор метод(при создании объекта)
	# получает экземпляр драйвера и url,
	# сохраняем как атрибуты класса
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)
	def open(self):
		self.browser.get(self.url)
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True


