from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Framework.BasePage import BasePage

fast_search_input = "//*[@id='search-and-pay-container']//input[@type='text']"
fast_search_result_array = "//*[@id='search-and-pay-container']//div[@data-qa-node='Tag']/div/div/div[@data-qa-node='Text']"
# search_button = "//*[@id='search-and-pay-container']//svg"
communal_payments_button = "//div[contains(@class, 'Payments__categories')]//a[contains(@href, 'kommunalnie-platezhi')]"


class PaymentsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.wait_to_load()

    def wait_to_load(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, communal_payments_button)))

    def fill_fast_search(self, text):
        self.driver.find_element_by_xpath(fast_search_input).send_keys(text)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, fast_search_result_array)))

    def get_provider_name_from_search_by_index(self, index=0):
        providers = self.driver.find_elements_by_xpath(fast_search_result_array)
        return providers[index].text

    def open_payment_form_from_search_by_index(self, index=0):
        providers = self.driver.find_elements_by_xpath(fast_search_result_array)
        providers[index].click()
        from Framework.CommunalPaymentsFormPage import CommunalPaymentsPage
        return CommunalPaymentsPage(self.driver)

    def open_communal_payments_page(self):
        self.driver.find_element_by_xpath(communal_payments_button).click()
        from Framework.CommunalPaymentsPage import CommunalPaymentsPage
        return CommunalPaymentsPage(self.driver)
