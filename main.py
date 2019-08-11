from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Firefox(executable_path='D:\geckodriver\geckodriver.exe')
driver = webdriver.phantomjs

driver.get("http://checkyourflight.info")
departdate = driver.find_element_by_id('fecha_salida')
departdate.send_keys('10/08/2019')
print(departdate)
select = Select(driver.find_element_by_id('flight'))

for option in select:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
driver.close()