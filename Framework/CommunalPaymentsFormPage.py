from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Framework.BasePage import BasePage

know_arrears_button = "//a[@href='/zhku-moskva/']"
payment_button = "(//a[contains(@href, 'zhku-moskva/oplata')])[1]"
payer_code_input = "//*[@id='payerCode']"
payer_code_error_element = payer_code_input + "/../../../..//div[contains(@class, 'error-message')]"
period_input = "//*[@id='period']"
period_error_element = period_input + "/../../../../..//div[contains(@class, 'error-message')]"
sum_of_payment_input = "(//input[@data-qa-file='StatelessInput'])[2]"
sum_of_payment_error_element = sum_of_payment_input + "/../../../..//div[contains(@class, 'error-message')]"
pay_button = "//h2"


class CommunalPaymentsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.wait_to_load()

    def wait_to_load(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, payment_button)))

    def switch_to_know_arrears(self):
        self.driver.find_element_by_xpath(know_arrears_button).click()

    def switch_to_pay(self):
        self.driver.find_element_by_xpath(payment_button).click()

    def fill_payer_code(self, text):
        self.driver.find_element_by_xpath(payer_code_input).send_keys(text)

    def fill_period(self, text):
        self.driver.find_element_by_xpath(period_input).send_keys(text)

    def fill_sum_of_payment(self, text):
        self.driver.find_element_by_xpath(sum_of_payment_input).send_keys(text)

    def click_pay_button(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, pay_button)))
        self.driver.find_element_by_xpath(pay_button).click()

    def get_payer_code_error(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, payer_code_error_element)))
        return self.driver.find_element_by_xpath(payer_code_error_element).text

    def get_period_error(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, period_error_element)))
        return self.driver.find_element_by_xpath(period_error_element).text

    def get_sum_of_payment_error(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, sum_of_payment_error_element)))
        return self.driver.find_element_by_xpath(sum_of_payment_error_element).text
