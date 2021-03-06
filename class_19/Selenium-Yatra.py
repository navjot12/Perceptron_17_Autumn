# Need to download the Chrome webdriver. Also need to install selenium using pip.

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')					# Provide correct path to the downloaded webdriver
driver.get("https://www.yatra.com/")
time.sleep(5)

dep = driver.find_element_by_id('BE_flight_origin_city')
dep.clear()
dep.send_keys("Delhi")
time.sleep(1)
dep.send_keys(Keys.RETURN)

arr = driver.find_element_by_id('BE_flight_arrival_city')
arr.clear()
arr.send_keys("Mumbai")
time.sleep(1)
arr.send_keys(Keys.RETURN)

driver.find_element_by_id("ico-cal").click()
driver.find_element_by_id("td_2017_11_22").click()
driver.find_element_by_id("BE_flight_flsearch_btn").click()

time.sleep(30)
driver.close()
