import os, time

from pages.base_page_101internet import WebPage
from pages.elements import WebElement, ManyWebElements

class SendRequestPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://piter-online.net/leningradskaya-oblast/orders/home?tariff_id=102134021'

        super().__init__(web_driver, url)

     # Поле "ВАШЕ ИМЯ" на странице тарифа
    name_field = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')

    # Поле "МОБИЛЬНЫЙ ТЕЛЕФОН" на странице тарифа
    phone_number_field = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div[2]/input')

    # Кнопка "ОСТАВИТЬ ЗАЯВКУ" на странице тарифа
    keep_request_button = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[6]/div')

