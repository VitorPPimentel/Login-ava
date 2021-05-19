from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, context):
        self.context = context
        self.url = context.variables["url"]

    def find_element(self, *loc):
        return self.context.browser.find_element(*loc)

    def navigate_to(self):
        self.context.browser.get(self.url)

    def click(self, element):
        WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
          expected_conditions.element_to_be_clickable(element)
        )

        self.context.browser.execute_script('arguments[0].click();', element)

    def __getattr__(self, item):
        if item in self.locators.keys():
            WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
                expected_conditions.visibility_of_element_located(self.locators[item])
            )

            loc = self.find_element(*self.locators[item])
            return loc
        else:
            raise AttributeError("'BasePage' object has no attribute '{0}'", item)