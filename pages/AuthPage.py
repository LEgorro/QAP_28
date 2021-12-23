import os

from pages.base import WebPage
from pages.elements import WebElement



class AuthPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://www.labirint.ru/cabinet/'

        super().__init__(driver, url)

    # Auth field
    input_field = WebElement(xpath='//input[@value="+7"]')

    # Enter button
    enter_button = WebElement(xpath='//input[@id="g-recap-0-btn"]')

    # Text with user code in user cabinet
    text_code = WebElement(xpath='//span[starts-with(text(), " Код скидки")]')

    # Message about invalid user code
    error_code_msg = WebElement(xpath='//small[contains(text(), "Введенного кода не существует")]')

    # Message about whitespaces
    error_whitespaces_msg = WebElement(xpath='//small[contains(text(), "Нельзя использовать символ « »")]')

    # Message about invalid phone format
    error_phone_msg = WebElement(xpath='//small[contains(text(), "Неверный формат телефона")]')

    # Message about special character
    error_wrong_char_msg = WebElement(xpath='//small[contains(text(), "Нельзя использовать символ «")]')

    # Message about cyrillic character
    error_cyrillic_char_msg = WebElement(xpath='//span[@data-notification-text-rus]')

    # My labirint button
    my_labirint_button = WebElement(xpath='//a[@class = "b-header-b-personal-e-link top-link-main '
                                          'top-link-main_cabinet  js-b-autofade-wrap"]')

    # Logout button
    logout_button = WebElement(xpath='//a[@href="/authorization/logout/"]')

    # Сoupon reminder
    coupon_reminder = WebElement(xpath='//span[contains(text(), "Купон на")]')