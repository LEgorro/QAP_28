import os

from pages.base import WebPage
from pages.elements import WebElement


class CheckoutPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("CHECKOUT_URL") or 'https://www.labirint.ru/cart/checkout/'

        super().__init__(driver, url)

    #
    initializing_checkout_button = WebElement(xpath='//button[@type="submit" and contains(text(), "Начать оформление")]')

    # Кнопка изменения города доставки
    change_region_post_button = WebElement(xpath='//span[@title="Выбрать другой город/страну"]')

    # Поле для ввода города доставки
    input_region_post_field = WebElement(xpath='//input[@id="region-post"]')

    # Подсказка при наборе города
    hint_for_region = WebElement(xpath='//div[@class="b-region-win-list js-regions-list"]/ul/li')

    # Кнопка самовывоза
    pickup_button = WebElement(xpath='//span[@title="Тип доставки" and contains(text(), "Самовывоз")]')

    pickup_change_button = WebElement(xpath='//span[contains(text(), "Поменять")]')

    # Поле для поиска пункта самовывоза по адресу
    input_point_address_field = WebElement(xpath='//input[@placeholder="Найти по станции метро или улице"]')

    # Первый предлагаемый пункт самовывоза
    first_pickup_point = WebElement(xpath='//div[contains(text(), "Арбатская")]')

    # Адрес первого пункта
    first_pickup_point_address = WebElement(xpath='//div[contains(text(), "Арбатская")]/..')

    final_address = WebElement(xpath='//span[@class="b-deliv-im-head-e-subname g-alttext-greylight"]')

    # Кнопка "Заберу отсюда", появляющаяся при выборе пункта самовывоза
    pickup_here = WebElement(xpath='//div[@class="b-yamap-balloon-e-button"]')

    # Кнопка "Предоплата"
    prepaid_button = WebElement(xpath='//label[contains(@class, "b-radio-payment-kassa") and '
                                      'not(contains(@class, "b-radio-m-checked"))]//'
                                      'span[contains(text(), "Предоплата")]')

    # Отмеченная кнопка "Предоплата"
    prepaid_checked_button = WebElement(xpath='//label[contains(@class, "b-radio-m-checked")]//'
                                              'span[contains(text(), "Предоплата")]')

    # Кнопка "При получении"
    cash_button = WebElement(xpath='//label[contains(@class, "b-radio-payment-cash") and '
                                   'not(contains(@class, "b-radio-m-checked"))]//'
                                   'span[contains(text(), "При получении")]')

    # Отмеченная кнопка "При получении"
    cash_chechked_button = WebElement(xpath='//label[contains(@class, "b-radio-m-checked")]//'
                                            'span[contains(text(), "При получении")]')

    # Зачеркнутая надпись "тип оплаты"
    payment_type_chosen = WebElement(xpath='//span[contains(@class, "b-lefttofill-items-e-item-m-filled") and '
                                           'contains(text(), "тип оплаты")]')

    # Кнопка для согласия на оповещения о прибытии товара
    notification_button_OFF = WebElement(xpath='//label[contains(@class, "checked")]/span[@class="checkbox-ui-text"]')

    # Отмеченная кнопка для согласия на оповещения о прибытии товара
    notification_button_ON = WebElement(xpath='//label[contains(@class, "checked")]/span[@class="checkbox-ui-text"]')