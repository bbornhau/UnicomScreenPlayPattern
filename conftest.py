import pytest
from  selenium import webdriver



@pytest.fixture(scope='class')
def browserFixture(headlessBrowser,browser):
	""" Takes the parameter headlessBrowser and sets a pytest variable to the requested webdriver"""
	#setup
	if browser == "firefox":
		options = webdriver.firefox.options.Options()
		options.headless=headlessBrowser
		pytest.varDriver=webdriver.Firefox(options=options)
	elif browser == "chrome":
		options = webdriver.chrome.options.Options()
		options.add_argument("--window-size=1920,1080")
		# options.add_argument("--start-maximized")
		options.headless=headlessBrowser
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		pytest.varDriver=webdriver.Chrome(chrome_options=options)
	pytest.varDriver.implicitly_wait(30)
	 
	yield
	#teardown
	pytest.varDriver.quit()


def pytest_addoption(parser):
	"""Pytest commandline addoption handler"""
	parser.addoption("--headless", action="store", default="True", help="Select headless mode for local execution default : True, values: True or False")
	parser.addoption("--browser", action="store", default="Firefox", help="Select browser for  execution default : Firefox,values: Firefox or Chrome")


@pytest.fixture(scope='class')
def headlessBrowser(request):
	"""Fixture that returns the value of the commandline option --headless"""
	return eval(request.config.getoption("--headless"))

@pytest.fixture(scope='class')
def browser(request):
	"""Fixture that returns the value of the commandline option --browser in lower case"""
	return request.config.getoption("--browser").lower()
