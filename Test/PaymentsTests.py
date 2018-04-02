from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

import Data.TestData as DATA
from Framework.MainPage import MainPage

class PaymentsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(DATA.CHROMEDRIVER)
        self.driver.get(DATA.TINKOFF_SITE)
        self.main_page = MainPage(self.driver)

    def test_check_payments(self):
        payments_page = self.main_page.open_payments()

        communal_page = payments_page.open_communal_payments_page()

        communal_page.change_region(DATA.MOSCOW_REGION)

        first_provider_name = communal_page.get_provider_name_by_index()
        self.assertEqual(DATA.ZHKU_MOSKVA, first_provider_name)
        zhku_moskva_payment_form = communal_page.open_payment_form_by_index()
        zhku_moskva_url = zhku_moskva_payment_form.driver.current_url

        zhku_moskva_payment_form.switch_to_pay()

        zhku_moskva_payment_form.click_pay_button()
        error_message = zhku_moskva_payment_form.get_payer_code_error()
        self.assertEqual(DATA.ERROR_MESSAGE_1, error_message)
        error_message = zhku_moskva_payment_form.get_period_error()
        self.assertEqual(DATA.ERROR_MESSAGE_1, error_message)
        error_message = zhku_moskva_payment_form.get_sum_of_payment_error()
        self.assertEqual(DATA.ERROR_MESSAGE_1, error_message)
        zhku_moskva_payment_form.fill_payer_code('0')
        zhku_moskva_payment_form.fill_period('0')
        zhku_moskva_payment_form.fill_sum_of_payment('0')
        zhku_moskva_payment_form.click_pay_button()
        error_message = zhku_moskva_payment_form.get_payer_code_error()
        self.assertEqual(DATA.ERROR_MESSAGE_2, error_message)
        error_message = zhku_moskva_payment_form.get_period_error()
        self.assertEqual(DATA.ERROR_MESSAGE_3, error_message)
        error_message = zhku_moskva_payment_form.get_sum_of_payment_error()
        self.assertEqual(DATA.ERROR_MESSAGE_4, error_message)
        zhku_moskva_payment_form.fill_sum_of_payment('15001')
        zhku_moskva_payment_form.click_pay_button()
        error_message = zhku_moskva_payment_form.get_sum_of_payment_error()
        self.assertEqual(DATA.ERROR_MESSAGE_5, error_message)

        zhku_moskva_payment_form.switch_to_know_arrears()
        payments_page = zhku_moskva_payment_form.open_payments()

        payments_page.fill_fast_search(first_provider_name)

        first_search_result = payments_page.get_provider_name_from_search_by_index()
        self.assertEqual(DATA.ZHKU_MOSKVA, first_search_result)

        zhku_moskva_payment_form = payments_page.open_payment_form_from_search_by_index()
        new_zhku_moskva = zhku_moskva_payment_form.driver.current_url
        self.assertEqual(zhku_moskva_url, new_zhku_moskva)

        payments_page = zhku_moskva_payment_form.open_payments()
        communal_page = payments_page.open_communal_payments_page()

        communal_page.change_region(DATA.ST_PETERSBURG_REGION)

        st_petersburg_provider_names = communal_page.get_all_provider_names()
        self.assertNotIn(DATA.ZHKU_MOSKVA, st_petersburg_provider_names)

    def tearDown(self):
        self.driver.quit()
