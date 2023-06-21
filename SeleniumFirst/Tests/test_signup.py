from selenium import webdriver
from selenium.webdriver.common.by import By

from Base.PageBase_test import *

PageBase = PageBase()

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    search = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search.send_keys("Im trying to learn automate").clickH()
    driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()


def test_tearDown():
    driver.close()
    driver.quit()
    print("done test")
