from pages.base import WebPage
from pages.elements import WebElement
from pages.MainPage import MainPage


def get_random_book_url(driver):
    page = MainPage(driver)
    page.product_cover.click()
    return driver.current_url

class ProductCardPage(WebPage):


    def __init__(self, driver, url=''):
        if not url:

            url = get_random_book_url(driver)

        super().__init__(driver, url)

    # Name of a book
    name = WebElement(xpath='//div[@class="prodtitle"]/h1')

    # Photo of a book
    photo = WebElement(xpath='//div[@id="product-image"]/img')

    # Cart button
    add_to_cart_button = WebElement(xpath='//span[text()="Добавить "]')

    # Place an order button
    place_an_order_button = WebElement(xpath='//a[@class="btn btn-small btn-more tobasket"]')

    # Cart count
    cart_count = WebElement(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    # Price of a book
    price = WebElement(xpath='//span[@class="buying-price-val-number"]')

    # Rate of a book
    rate = WebElement(xpath='//div[@id="rate"]')

    # Annotation of a book
    annotation = WebElement(xpath='//div[@id="product-about"]')

    # Articul of a book
    articul = WebElement(xpath='//div[@class="articul"]')

    # Breadcrumbs
    breadcrumbs = WebElement(xpath='//div[@id="thermometer-books"]')

