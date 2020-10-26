import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store',default='en',
                        help="Choose language: ru,en,... (etc)")

'''
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр 
language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком 
пользователя. Браузер должен объявляться в фикстуре browser и передаваться 
в тест как параметр.

pytest -s -v --browser_name=chrome test_parser.py
pytest -s -v --browser_name=firefox test_parser.py
'''


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_lang = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        # browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # browser = webdriver.Firefox()
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


