import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class SearchPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("SEARCH_URL") or 'https://www.labirint.ru/books/'

        super().__init__(driver, url)

    # Filtered field
    filtered_field = WebElement(xpath='//div[@class="filters-selected"]')

    # All filters button
    all_filters = WebElement(xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ")]')

    # Availability filters button
    availability_filters = WebElement(xpath='//span[contains(text(), "НАЛИЧИЕ")]')

    # In stock filter button in submenu
    in_stock_filter = WebElement(xpath='//li/label[contains(text(), "В наличии")]')

    # Pre-order filter button in submenu
    pre_order_filter = WebElement(xpath='//li/label[contains(text(), "Предзаказ")]')

    # Expected filter button in submenu
    expected_filter = WebElement(xpath='//li/label[contains(text(), "Ожидаются")]')

    # Out of stock filter button in submenu
    not_on_sale_filter = WebElement(xpath='//li/label[contains(text(), "Нет в продаже")]')

    # In stock filter ON text
    in_stock_filter_ON = WebElement(xpath='//div[@class="filter-reset__content" and contains(text(), "В наличии")]')

    # Pre_order filter ON text
    pre_order_filter_ON = WebElement(xpath='//div[@class="filter-reset__content" and contains(text(), "Предзаказ")]')

    # Expected filter ON text
    expected_filter_ON = WebElement(xpath='//div[@class="filter-reset__content" and contains(text(), "Ожидаются")]')

    # Out of stock filter ON text
    not_on_sale_filter_ON = WebElement(xpath='//div[@class="filter-reset__content" and contains(text(), "Нет в '
                                             'продаже")]')

    # Accept button in availability filters
    accept_availability_filters = WebElement(xpath='//span[@class="navisort-part navisort-filter navisort-part-2 '
                                                   'fleft"]//input[@type="submit"]')

    # Price filters
    price_filters = WebElement(xpath='//span[contains(text(), "ЦЕНА")]')

    # Price min input field
    price_min = WebElement(xpath='//input[@name="price_min"]')

    # Price max input field
    price_max = WebElement(xpath='//input[@name="price_max"]')

    # Accept button in price filters
    accept_price_filters = WebElement(xpath='//span[@class="navisort-part navisort-filter navisort-part-3 '
                                                   'fleft"]//input[@type="submit"]')

    # Filtered product prices in product cards
    product_prices = ManyWebElements(xpath='//div[@data-title="Все в жанре «Книги»"]//span[@class="price-val"]/span')

    # Genre filters
    genre_filters = WebElement(xpath='//span[contains(text(), "УТОЧНИТЬ ЖАНР")]')

    # Fiction
    fiction = WebElement(xpath='//div[contains(text(), " ХУДОЖЕСТВЕННАЯ ЛИТЕРАТУРА")]')

    # Classical prose
    classical_prose = WebElement(xpath='//div[contains(@class, "b-genre-title-level-1") and contains(text(), '
                                       '" Классическая проза")]')

    # All classical prose
    all_classical_prose = WebElement(xpath='//a[contains(@class, "b-genre-title-level-2") and contains(text(), '
                                           '" Вся классическая проза")]')

    # Filtered product cards
    product_cards = ManyWebElements(xpath='//div[@data-title="Все в жанре «Книги»"]//div[@class="product need-watch '
                                          'watched"]')

    # Publisher filters
    publishers = WebElement(xpath='//div[contains(text(), "ИЗДАТЕЛЬСТВА")]')

    # Publisher AST
    publisher_AST = WebElement(xpath='//span[@class="b-radio-txt" and contains(text(), "АСТ")]')

    # Accept button in all filters
    accept_all_filters = WebElement(xpath='//input[@class="show-goods__button"]')