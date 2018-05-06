import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.PhantomJS()
driver.get("https://m.facebook.com/?_rdr")
driver.find_element_by_css_selector('._56bg._4u9z._5ruq').send_keys("fhgjhmacu@wjhndxn.xyz")
driver.find_element_by_id("u_0_2").send_keys("lenpretest")
time.sleep(1)   
driver.find_element_by_id("u_0_7").click()
time.sleep(1)
driver.get("https://m.facebook.com/actual4chan2/?fref=ts")
time.sleep(1)
driver.find_element_by_css_selector('._56bz._54k8._5c9u._5caa').click()
time.sleep(2)

#print(driver.page_source )
