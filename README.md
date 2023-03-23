# TestCase_101Internet
# Автоматизированное тестирование процесса отправки заявки на подключение тарифов провайдера на сайте по поиску провайдеров https://piter-online.net/ (101 Internet) с помощью Selenium.
В папке pages находятся файлы, описывающие шаблоны страниц и непосредственно страницы сайта https://piter-online.net/.

В файле pages/base_page_101internet.py содержится реализацию шаблона PageObject для Python.

В файле pages/elements.py содержится вспомогательный класс для определения веб-элементов на веб-страницах.

В файле pages/config_101internet.py содержится информация о валидных данных, необходимых для поиска тарифов провайдера и подачи заявки на подключение.

В файле pages/main_page_101internet.py содержится класс главной страницы сайта 101 Internet (Санкт-Петербург) https://piter-online.net/.

В файле pages/send_request_page_101internet.py содержится класс страницы с формой отправки заявки для определенного тарифа на сайте 101 Internet (Санкт-Петербург) https://piter-online.net/leningradskaya-oblast/orders/home?tariff_id=102134021.

В файле requirements.txt находится список требуемых к установке библиотек.

# ИНСТРУКЦИЯ ПО ЗАПУСКУ:
1. Скачать драйвер для браузера Google Chrome - https://chromedriver.chromium.org/downloads

2. Установить все требуемые библиотеки из файла requirements.txt с помощью команды:
pip install -r requirements.txt

3. Запустить разработанные тесты с помощью команды:
python -m pytest -v --driver Chrome --driver-path C:/Documents/chromedriver.exe tests/test_101internet.py
(где C:/Documents - папка с расположением драйвера Chrome)
