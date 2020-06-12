from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import json
from tinydb import TinyDB, Query, where

configs = json.loads(open('config/app.json').read())
proxies = TinyDB('db/bot.json').table('proxies')
links = TinyDB('db/bot.json').table('links')

# driver_path = ChromeDriverManager().install()
# PROXY = "49.12.75.192:3128"  # IP:PORT or HOST:PORT
# PROXY = "178.62.113.81:3128"  # IP:PORT or HOST:PORT
# PROXY = "98.143.145.30:62353"  # IP:PORT or HOST:PORT
# PROXY = "169.57.1.85:8123"  # IP:PORT or HOST:PORT
# PROXY = "134.209.29.120:8080"  # IP:PORT or HOST:PORT


chrome_options = webdriver.ChromeOptions()
if 'use_proxies' in configs and configs['use_proxies']:
    PROXY = "82.119.170.106:8080"  # IP:PORT or HOST:PORT
    chrome_options.add_argument('--proxy-server=%s' % PROXY)

# PROXY = "82.119.170.106:8080"  # IP:PORT or HOST:PORT
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
# driver = webdriver.Chrome(ROOT_DIR + '/drivers/browsers/chromedriver.75.exe')
driver_path = ROOT_DIR + '/drivers/browsers/chromedriver.83.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
# chrome.get("https://python.org")
# chrome.get("https://whatismyipaddress.com/")

for l in links:
    driver.get(l['url'])
    timeout = 50
    print("start sleep for" + str(l['url']))
    time.sleep(10)
    print("end sleep for" + str(l['url']))
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.TAG_NAME, "span"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "skip_button"))).click()
    time.sleep(10)
    driver.quit()
    time.sleep(10)

# try:
#     element_present = EC.presence_of_element_located((By.LINK_TEXT, 'SKIP THIS AD'))
#     print(element_present)
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from webdriver_manager.chrome import ChromeDriverManager
# driver_path = ChromeDriverManager().install()
# options = webdriver.ChromeOptions()
# proxy = Proxy()
# proxy.proxyType = ProxyType.MANUAL
# proxy.autodetect = False
# proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = "49.12.75.192:3128"
# options.Proxy = proxy
# options.add_argument("ignore-certificate-errors")
# driver = webdriver.Chrome(executable_path=driver_path, options=options)
# driver.get("https://python.org")
