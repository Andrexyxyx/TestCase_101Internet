from selenium.webdriver.common import keys

from pages.main_page_101internet import MainPage
from pages.config_101internet import valid_street, valid_number_home, valid_name, valid_phone
import time
from pages.send_request_page_101internet import SendRequestPage

import time
from selenium.webdriver.common.keys import Keys

import requests

# Команда для запуска тестов
# python -m pytest -v --driver Chrome --driver-path C:/Documents/chromedriver.exe tests/test_101internet.py

def test1_send_request_rates(web_browser):
    """Проверка отправки заявки. Проверяем, что отправка заявки на подключение тарифа провайдера возвращает
    код статуса 200"""
    page_main = MainPage(web_browser)
    page_main.scroll_down(250)

    page_main.street_field.send_keys(valid_street)
    time.sleep(2)
    page_main.street_field.send_keys(Keys.RIGHT)
    page_main.street_field.send_keys(Keys.RETURN)
    time.sleep(2)
    page_main.number_home_field.send_keys(valid_number_home)
    time.sleep(1)

    page_main.type_connection_list.click()
    page_main.apartment_list.click()
    time.sleep(1)

    page_main.show_rates_button.click()

    page_main.close_button.click()
    page_main.scroll_down(500)
    page_main.plug_by_promo_button.click()

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200

    page_request = SendRequestPage(web_browser)
    page_request.scroll_down(500)
    page_request.name_field.send_keys(valid_name)
    page_request.phone_number_field.send_keys(valid_phone)
    page_request.keep_request_button.click()
    time.sleep(1)
    page_request_url = page_request.get_current_url()
    res = requests.get(page_request_url)
    status = res.status_code
    assert status == 200






