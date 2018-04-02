from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

payments_button = "//div[contains(@class, 'SecondMenu')]//a[@href='/payments/']"
regions_array = "//div[contains(@class, 'uiRegions__item')]//a/span"


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open_payments(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, payments_button)))
        self.driver.find_element_by_xpath(payments_button).click()
        from Framework.PaymentsPage import PaymentsPage
        return PaymentsPage(self.driver)

    def choose_region(self, region):
        regions = self.driver.find_elements_by_xpath(regions_array)
        for reg in regions:
            if region in reg.text:
                reg.click()
                break
