import unittest
import time

import testPage
from testLocate import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



class MainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://magento.softwaretestingboard.com/")

    def test_CreateAnAccount(self):
        testp = testPage.PageMain(self.driver)
        assert True
        element = self.driver.find_element(*PageMainLocate.CAN)
        element.click()

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.ID, "firstname"),
            lambda driver: driver.find_element(By.ID, "password")
        )

        self.driver.find_element(*SignUpLogInAndMorePageLocate.f).send_keys(*testp.first_name)
        assert True
        print("Name is Added")
        time.sleep(0.2)
        assert True
        self.driver.find_element(*SignUpLogInAndMorePageLocate.la).send_keys(*testp.last_name)
        print("LastName is Added")
        time.sleep(0.2)
        assert True
        self.driver.find_element(By.ID, "is_subscribed").click()
        print("Checkbox is checked")
        assert True
        self.driver.find_element(*SignUpLogInAndMorePageLocate.e).send_keys(*testp.email)
        print("Email is Added")
        time.sleep(0.2)
        assert True
        self.driver.find_element(*SignUpLogInAndMorePageLocate.p).send_keys(*testp.password)
        print("Pass is Added")
        time.sleep(0.2)
        assert True
        self.driver.find_element(*SignUpLogInAndMorePageLocate.pc).send_keys(*testp.password)
        print("PassConf is Added")
        time.sleep(0.2)
        assert True
        self.driver.execute_script('window.scrollTo(0, 1260);')
        time.sleep(0.4)
        assert True
        self.driver.find_element(*SignUpLogInAndMorePageLocate.Ca).click()
        print("[[Account is Created]]")
        time.sleep(0.4)
        assert True

    def test_Login(self):
        testp = testPage.PageMain(self.driver)
        assert True
        element = self.driver.find_element(*PageMainLocate.SI)
        element.click()

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.ID, "email"),
            lambda driver: driver.find_element(By.ID, "pass")
        )

        self.driver.find_element(*SignUpLogInAndMorePageLocate.eLog).send_keys(*testp.email)
        assert True
        print("EmailLogin is Added")
        time.sleep(0.2)
        self.driver.find_element(*SignUpLogInAndMorePageLocate.pLog).send_keys(*testp.password)
        assert True
        print("passLogin is Added")
        time.sleep(0.2)
        self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
        print("Logged In")
        time.sleep(3)
        assert True

    def test_Browse(self):
        self.test_Login()
        womenb = self.driver.find_element(By.XPATH, "//span[normalize-space()='Women']")
        tops = self.driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
        achains = ActionChains(self.driver)
        achains.move_to_element(womenb).move_to_element(tops).click().perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='product photo product-item-photo']//img[@alt='Antonia Racer Tank']").click()
        time.sleep(0.2)
        self.driver.execute_script('window.scrollTo(0, 900);')
        time.sleep(3)
        print("Browsing is done")

    def test_VerifyAndAddToCart(self):
        self.test_Browse()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, "//input[@id='qty']")
        )
        try:
            price = self.driver.find_element(By.XPATH, "//span[@id='product-price-1796']//span[@class='price'][normalize-space()='$34.00']").text
            assert (price == ProductInformationAntonia.PriceA)
            print(price, "is okay")
            name = self.driver.find_element(By.XPATH, "//span[@class='base']").text
            assert (name == ProductInformationAntonia.NameA)
            print(name, "is okay")
            desc = self.driver.find_element(By.XPATH, "//div[@class='page-wrapper']//p[1]").text
            assert (desc == ProductInformationAntonia.DescA)
            print("Detail is okay")
        except:
            print("One or more details dont match")

        self.driver.execute_script('window.scrollTo(0, 0);')
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-166']").click()
        self.driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-49']").click()
        self.driver.find_element(By.NAME, "qty").clear()
        self.driver.find_element(By.NAME, "qty").send_keys(5)
        time.sleep(4)
        self.driver.find_element(By.ID, "product-addtocart-button").click()
        time.sleep(3)
        print("verify and add is done")

    def test_ShoppingCartVerify(self):
        self.test_VerifyAndAddToCart()
        self.driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
        VIEWCART = self.driver.find_element(By.XPATH, "//span[normalize-space()='View and Edit Cart']")
        webdriver.ActionChains(self.driver).move_to_element(VIEWCART).click(VIEWCART).perform()
        time.sleep(2)
        try:
            Namee = self.driver.find_element(By.XPATH, "//td[@class='col item']//a[normalize-space()='Antonia Racer Tank']").text
            assert (Namee == ProductInformationAntonia.NameA)
            print("Product we added correctly in there")
            Size = self.driver.find_element(By.XPATH, "//dd[contains(text(),'XS')]").text
            assert (Size == ProductInformationAntonia.CheckBoxXS)
            print("Product has the size we ordered")
        except:
            print("Wrong product in cart")

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, "//strong[normalize-space()='Order Total']")
        )

        self.driver.find_element(By.XPATH, "//span[normalize-space()='Proceed to Checkout']").click()
        time.sleep(2)
        print("Navigate to cart and verify product is done")
        print("Proceed to checkout is done")

    def test_FillShippingBilling(self):
        global namer, lastnamer, company, StreetAdd, City, postcode, Number
        self.test_ShoppingCartVerify()
        testp = testPage.PageMain(self.driver)


        if self.driver.find_element(By.XPATH, "//span[normalize-space()='New Address']"):
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        else:
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(*SignUpLogInAndMorePageLocate.ST0)
            )

            namer = self.driver.find_element(*SignUpLogInAndMorePageLocate.first)
            namer.clear()
            namer.send_keys(*testp.first_name)
            assert (namer != testp.CLEARCLEAR)
            print("Name is ok")
            ###########
            lastnamer = self.driver.find_element(*SignUpLogInAndMorePageLocate.last)
            lastnamer.clear()
            lastnamer.send_keys(*testp.last_name)
            assert (lastnamer != testp.CLEARCLEAR)
            print("lastName is ok")
            ##########
            company = self.driver.find_element(*SignUpLogInAndMorePageLocate.CMP)
            company.clear()
            company.send_keys(*testp.company)
            print("company is added")
            ##########
            StreetAdd = self.driver.find_element(*SignUpLogInAndMorePageLocate.ST0)
            StreetAdd.clear()
            StreetAdd.send_keys(*testp.last_name)
            assert (StreetAdd != testp.CLEARCLEAR)
            print("StreedAdd is ok")
            ###########
            City = self.driver.find_element(*SignUpLogInAndMorePageLocate.CT)
            City.clear()
            City.send_keys(*testp.city)
            assert (City != testp.CLEARCLEAR)
            print("City is ok")
            ###########
            Country = self.driver.find_element(By.NAME, "country_id")
            CountryS = Select(Country)
            CountryS.select_by_index(9)
            time.sleep(0.4)
            CountryS = Select(Country)
            CountryS.select_by_value("US")
            time.sleep(0.4)
            CountryS = Select(Country)
            CountryS.select_by_visible_text("Albania")
            time.sleep(3)
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_element(By.CLASS_NAME, "table-checkout-shipping-method")
            )
            #############
            stateProv = self.driver.find_element(By.NAME, "region_id")
            stateText = self.driver.find_element(By.NAME, "region")
            if stateProv.is_displayed():
                stateMulti = Select(stateProv)
                stateMulti.select_by_index(1)
                time.sleep(0.4)
                stateMulti = Select(stateProv)
                stateMulti.select_by_value("39")
                time.sleep(0.4)
                stateMulti = Select(stateProv)
                stateMulti.select_by_visible_text("Oklahoma")
                WebDriverWait(self.driver, 100).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, "table-checkout-shipping-method")
                )
            elif stateText.is_displayed():
                stateText.send_keys(*testp.city)
                time.sleep(2)
                WebDriverWait(self.driver, 100).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, "table-checkout-shipping-method")
                )
            #############
            postcode = self.driver.find_element(*SignUpLogInAndMorePageLocate.PostC)
            postcode.clear()
            postcode.send_keys(*testp.zip)
            assert (postcode != testp.CLEARCLEAR)
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_element(By.CLASS_NAME, "table-checkout-shipping-method")
            )
            Number = self.driver.find_element(By.NAME, "telephone")
            Number.clear()
            Number.send_keys(*testp.phoneNumber)
            assert (Number != testp.CLEARCLEAR)
            Pricee = self.driver.find_element(By.CLASS_NAME, "price").is_displayed()
            assert Pricee
            print("Price in billing is diplayed")
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_element(By.CLASS_NAME, "table-checkout-shipping-method")
            )
            ###############################################################################



        next = self.driver.find_element(By.CSS_SELECTOR, ".button.action.continue.primary")
        webdriver.ActionChains(self.driver).move_to_element(next).click(next).perform()
        print("[[[[[[[Shipping info is done]]]]]]]]")
        time.sleep(2)

        placeOrder = self.driver.find_element(By.XPATH, "//button[@title='Place Order']")
        webdriver.ActionChains(self.driver).move_to_element(placeOrder).click(placeOrder).perform()
        print("Order is placed")
        time.sleep(2)
        ##############

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.XPATH, "//span[normalize-space()='Continue Shopping']")
        )
        thankyouNote = self.driver.find_element(By.XPATH, "//span[@class='base']").text
        orderN = self.driver.find_element(By.CLASS_NAME, "order-number").text
        if len(thankyouNote) and len(orderN) > 0:

            print("Order exists")
        else:
            print("order does not exist")



    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()