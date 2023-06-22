# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
#
# class PageBase:
#
#     def __init__(self, driver):
#         self._driver = driver
#         self._wait = WebDriverWait(self._driver, 10)
#
#     def click_highlight_button(self, webelement):
#         el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
#         self._highlight(el, "yellow")
#         el.click()
#
#     def _highlight(self):
#         driver = self._parent
#         original_style = self.get_attribute("Style")
#         driver.execute_script("arguments[0].setAttribute('Style', arguments[1]", self, "border: 2px solid yellow")
#         WebDriverWait(driver, 1).until(expected_conditions.staleness_of(self))
#         driver.execute_script("arguments[0].setAttribute('Style', arguments[1]", self, original_style)
