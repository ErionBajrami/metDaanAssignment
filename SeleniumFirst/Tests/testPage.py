# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from testLocate import *


# class EmailAddress(ElementPageBase):
#     locator = "email"
#
#
# class Mbiemri(ElementPageBase):
#     locator = "lastname"
#
#
# class Emri(ElementPageBase):
#     locator = "firstname"
#
#
# class Password(ElementPageBase):
#     locator = "password"
#
#
# class PasswordConf(ElementPageBase):
#     locator = "password_confirmation"



class PageBase(object):
    def __init__(self, driver):
        self.driver = driver


class PageMain(PageBase):

    # Emri_Acc = Emri()
    # Mb_Acc = Mbiemri()
    # Email_Acc = EmailAddress()
    # Pass_Acc = Password()
    # PassConf_Acc = PasswordConf()

    first_name = "Erion"
    last_name = "Bajrami"
    email = "erionbajrami@test.com"
    password = "Test123123"
    phoneNumber = "048 860 710"
    zip = "60000"
    company = "MetDaan"
    street_Address = "Isuf Kiki nr 6"
    city = "Gjilan"
    CLEARCLEAR = None


    # def click_highlight_button(self, webelement):
    #     el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
    #     self._highlight(el, "yellow")
    #     el.click()
    #
    # def _highlight(self):
    #     driver = self._parent
    #     original_style = self.get_attribute("Style")
    #     driver.execute_script("arguments[0].setAttribute('Style', arguments[1]", self, "border: 2px solid yellow")
    #     WebDriverWait(driver, 1).until(expected_conditions.staleness_of(self))
    #     driver.execute_script("arguments[0].setAttribute('Style', arguments[1]", self, original_style)
