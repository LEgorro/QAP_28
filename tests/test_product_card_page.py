import pytest
from pages.ProductCardPage import ProductCardPage

@pytest.fixture(scope="function")
def page(driver):
    return ProductCardPage(driver)


def test_is_there_product_name_on_book_card(driver, page):
    assert page.name.is_presented()


def test_is_there_product_photo_on_book_card(driver, page):
    assert page.photo.is_presented()


def test_is_there_add_to_cart_button_on_book_card(driver, page):
    assert page.add_to_cart_button.is_presented()


def test_is_there_price_on_book_card(driver, page):
    assert page.price.is_presented()


def test_is_there_rate_on_book_card(driver, page):
    assert page.rate.is_presented()


def test_is_there_annotation_on_book_card(driver, page):
    assert page.annotation.is_presented()


def test_is_there_articul_on_book_card(driver, page):
    assert page.articul.is_presented()


def test_is_there_breadcrumbs_on_book_card(driver, page):
    assert page.breadcrumbs.is_presented()


@pytest.mark.smoke
def test_add_book_to_cart_on_book_card(driver, page):
    page.add_to_cart_button.click()
    assert page.place_an_order_button.is_presented()


@pytest.mark.smoke
def test_cart_logo_change_num_when_book_added_on_book_card(driver, page):
    num = int(page.cart_count.get_text())
    page.add_to_cart_button.click()
    page.place_an_order_button.wait_until_not_visible()
    assert int(page.cart_count.get_text()) == num + 1