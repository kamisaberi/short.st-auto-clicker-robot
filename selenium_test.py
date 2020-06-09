from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType

import os

driver_path = ChromeDriverManager().install()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
# driver = webdriver.Chrome(ROOT_DIR + '/drivers/browsers/chromedriver.75.exe')

capabilities = webdriver.DesiredCapabilities.CHROME
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "194.26.180.142:80"
prox.socks_proxy = "194.26.180.142:80"
prox.ssl_proxy = "194.26.180.142:80"
prox.add_to_capabilities(capabilities)

options = webdriver.ChromeOptions()
options.Proxy = prox
# options.add_argument("ignore-certificate-errors")
# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities)
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get("http://www.python.org")

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()






# PROXY = "109.75.47.248:37926"  # IP:PORT or HOST:PORT
# PROXY = "194.26.180.142:80"  # IP:PORT or HOST:PORT
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
# chrome.get("http://python.org")

# from selenium import webdriver
# PROXY = "194.26.180.142:80"  # IP:PORT or HOST:PORT
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome = webdriver.Chrome(options=chrome_options)
# chrome.get("http://whatismyipaddress.com")
