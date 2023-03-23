import os, time

from pages.base_page_101internet import WebPage
from pages.elements import WebElement, ManyWebElements

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://piter-online.net/'

        super().__init__(web_driver, url)

     # Поле "Введите улицу" на главной странице
    street_field = WebElement(xpath='//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/input')

    # Поле "Дом" на главной странице
    number_home_field = WebElement(xpath='//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input')

    # Выпадающий список "Тип подключения" на главной странице
    type_connection_list = WebElement(xpath='//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/input')

    # Позиция "В квартиру" в выпадающем списке "Тип подключения" на главной странице
    apartment_list = WebElement(xpath='//*[@id="forSelectField"]/div[1]/div/div/div/ul/li[1]')

    # Кнопка "ПОКАЗАТЬ ТАРИФЫ" на главной странице
    show_rates_button = WebElement(xpath='//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div')

    # Кнопка "ЗАКРЫТЬ" для всплывающего окна на странице с результатами поиска тарифов
    close_button = WebElement(xpath='//*[@id="root"]/div/div[4]/div/div/div/div/div')

    # Кнопка "ПОДКЛЮЧИТЬ ПО АКЦИИ" на странице с результатами поиска тарифов
    plug_by_promo_button = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div[2]/div[2]/a')
