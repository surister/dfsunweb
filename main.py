from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path='D:\geckodriver\geckodriver.exe')


driver.get("http://checkyourflight.info")
driver.find_element_by_id('fecha_salida').click()
driver.find_element_by_id('fecha_salida').send_keys('2019-08-14')
driver.find_element_by_id('fecha_salida').click()
sleep(1)
flight_element = driver.find_element_by_xpath("//select[@id='flight']")
flights = flight_element.find_elements_by_tag_name("option")
for flight in flights:
    flight.click()
    print(flight.get_attribute('value'))
    sleep(1)
    element_hotel = driver.find_element_by_xpath("//select[@id='hoteles']")
    hotels = element_hotel.find_elements_by_tag_name("option")
    for hotel in hotels:
        hotel.click()
        print(hotel.get_attribute('value'))
sleep(100)

driver.close()
