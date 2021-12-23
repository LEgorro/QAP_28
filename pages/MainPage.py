import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru'

        super().__init__(driver, url)

    # Main search field
    search = WebElement(id='search-field')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//*[@class="product need-watch watched"]')

    # Poblisher of the book in search results
    book_publisher = ManyWebElements(xpath='//a[@class="product-pubhouse__pubhouse"]')

    # Logo
    logo = WebElement(xpath='//span[@class = "b-header-b-logo-e-logo"]')

    # Messages button
    messages_button = WebElement(xpath='//a[@class = "b-header-b-personal-e-link top-link-main '
                                       'have-dropdown-touchlink top-link-main_notification"]')

    # My labirint button
    my_labirint_button = WebElement(xpath='//a[@class = "b-header-b-personal-e-link top-link-main '
                                          'top-link-main_cabinet  js-b-autofade-wrap"]')

    # Postponed button
    postponed_button = WebElement(xpath='//a[@class = "b-header-b-personal-e-link top-link-main '
                                        'top-link-main_putorder"]')

    # Cart button
    cart_button = WebElement(xpath='//a[@class = "b-header-b-personal-e-link top-link-main '
                                   'analytics-click-js cart-icon-js"]')

    # Contact button (header)
    contact_header_button = WebElement(xpath='//a[@href="/contact/" '
                                             'and @class="b-header-b-sec-menu-e-link"]')

    # Support button (header)
    support_header_button = WebElement(xpath='//a[@href="/support/" '
                                             'and @class="b-header-b-sec-menu-e-link"]')

    # Random book cover
    product_cover = WebElement(xpath='//a[@class="cover"]')

    # Search error
    search_error = WebElement(xpath='//div[@class="search-error"]/h1')


