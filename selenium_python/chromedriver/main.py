from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from auth_data import login, password
import pickle
import os
# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")


options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path=r"C:\Users\hp\Desktop\Программирование\Parsing\selenium\selenium_python\chromedriver\chromedriver.exe",
    options=options
)
driver.maximize_window()
# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:



    driver.get("https://agroexpo.com/es/catalogo-expositores")

    pageSource1 = [1, 2]
    time.sleep(3)

    caunt = 0
    pageSource = driver.page_source
    fileToWrite = open("../../page_source.html", "w", encoding='utf-8')
    fileToWrite.write(pageSource)
    fileToWrite.close()

    pageSource = len(pageSource)
    while True:
        try:
            if pageSource != len(pageSource1):

                pageSource = len(pageSource1)
                out = driver.find_element_by_id('cargarMas')
                out.click()
                time.sleep(2)
                caunt = caunt + 1

                pageSource1 = driver.page_source
                fileToWrite1 = open("../../page_source.html", "w", encoding='utf-8')
                fileToWrite1.write(pageSource1)
                fileToWrite1.close()
                print(caunt, pageSource, len(pageSource1))
            else:
                break
        except:
            print('error')
            break

    print(caunt)
    time.sleep(10)
    pageSource = driver.page_source
    fileToWrite = open("../../page_source.html", "w", encoding='utf-8')
    fileToWrite.write(pageSource)
    fileToWrite.close()


    print(len(pageSource))






# pageSource = driver.page_source
# print(pageSource)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



