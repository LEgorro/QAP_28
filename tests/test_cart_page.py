import pytest
from pages.CartPage import CartPage


@pytest.fixture(scope="function")
def page(driver):
    return CartPage(driver)


def test_cart_is_empty(driver, page):
    assert page.text_empty.is_presented()


def test_rigth_nums_of_product(driver_with_cookies, page):
    num = 0
    for i in page.quantity_of_products.get_attribute('value'):
        num += int(i)
    assert int(page.logo_cart_button.get_text()) == 0 \
           or \
           (num == \
            int(page.num_prod_in_cart_button.get_text()) == \
            int(page.logo_cart_button.get_text()))


@pytest.mark.smoke
def test_product_prices_equal_cart_sum(driver_with_cookies, page):
    sum = 0
    for price in page.product_prices.get_text():
        if price:
            sum += int(price.replace(" ", ""))
    assert int(page.cart_sum.get_text().replace(" ", "")) == sum


def test_increase_product_quantity(driver_with_cookies, page):
    quantity_before = int(page.quantity_of_product.get_attribute('value'))
    page.increase_product_button.click()
    assert int(page.quantity_of_product.get_attribute('value')) == quantity_before + 1


def test_lessen_product_quantity(driver_with_cookies, page):
    assert int(page.logo_cart_button.get_text()) != 0, 'Корзина пуста. Для этого теста в ней должен быть хотя бы один товар'
    quantity_before = int(page.quantity_of_product.get_attribute('value'))
    if quantity_before > 1:
        page.lessen_product_button.click()
        assert int(page.quantity_of_product.get_attribute('value')) == quantity_before - 1
    if quantity_before == 1:
        page.increase_product_button.click()
        assert int(page.quantity_of_product.get_attribute('value')) == quantity_before + 1
        page.lessen_product_button.click()
        assert int(page.quantity_of_product.get_attribute('value')) == quantity_before - 1


def test_clear_cart(driver_with_cookies, page):
    page.erase_cart_button.is_presented()
    page.erase_cart_button.click()
    assert page.text_empty.is_presented()
    page.restore_cart_button.click()