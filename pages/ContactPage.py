import os

from pages.base import WebPage
from pages.elements import WebElement


class ContactPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("CONTACT_URL") or 'https://www.labirint.ru/contact/'

        super().__init__(driver, url)

    # Connect with the operator on page
    connect_with_the_operator_button = WebElement(
        xpath='//div[@id="_support_call_number"]/a[@title="Соединить с оператором"]')

    # Phone number of support
    phone_number = WebElement(xpath='//a[contains(text(), "8 800 600-95-25")]')

    # E-mail of support
    e_mail = WebElement(xpath='//a[contains(text(), "shop@labirintmail.ru")]')