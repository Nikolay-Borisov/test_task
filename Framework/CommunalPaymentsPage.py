from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Framework.BasePage import BasePage

region_button_xpath = "//span[contains(@class, 'PaymentsCatalogHeader')]/span/span"
providers_array = "//ul[contains(@class, 'categoryProviders')]/li/span[2]/a/span"


class CommunalPaymentsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.wait_to_load()

    def wait_to_load(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, providers_array)))

    def change_region(self, region):
        region_button = self.driver.find_element_by_xpath(region_button_xpath)
        current_region = region_button.text
        if region not in current_region:
            region_button.click()
            self.choose_region(region)
            self.wait_to_load()

    def get_provider_name_by_index(self, index=0):
        providers = self.driver.find_elements_by_xpath(providers_array)
        return providers[index].text

    def open_payment_form_by_index(self, index=0):
        providers = self.driver.find_elements_by_xpath(providers_array)
        providers[index].click()
        from Framework.CommunalPaymentsFormPage import CommunalPaymentsPage
        return CommunalPaymentsPage(self.driver)

    def get_all_provider_names(self):
        names = []
        providers = self.driver.find_elements_by_xpath(providers_array)
        for provider in providers:
            names.append(provider.text)
        return names
