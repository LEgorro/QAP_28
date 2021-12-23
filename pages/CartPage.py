import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class CartPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("CART_URL") or 'https://www.labirint.ru/cart/'

        super().__init__(driver, url)

    # Empty cart text on page
    text_empty = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?")]')

    # Product cards in cart
    product_cards = ManyWebElements(xpath='//div[@class="product need-watch product_labeled product-cart"]')

    # Product prices
    product_prices = ManyWebElements(xpath='//span[@class="price-val"]/span')

    # Quantity of products in cart
    quantity_of_products = ManyWebElements(xpath='//input[@class="quantity"]')

    # Num of prodict in cart on top left button "My cart:"
    num_prod_in_cart_button = WebElement(xpath='//a[contains(text(),"Моя корзина: ")]/b')

    # Num of prodict in logo cart"
    logo_cart_button = WebElement(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    # Cart sum
    cart_sum = WebElement(xpath='//span[@id="basket-default-sumprice-discount"]')

    # Increase product button
    increase_product_button = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')

    # Lessen product button
    lessen_product_button = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')

    # Quantity of product
    quantity_of_product = WebElement(xpath='//input[@class="quantity"]')

    # Erase cart button
    erase_cart_button = WebElement(xpath='//a[contains(text(), "Очистить корзину")]')

    # Restore cart buton
    restore_cart_button = WebElement(xpath='//a[contains(text(), "Восстановить удаленное")]')