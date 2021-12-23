import pytest
from pages.SearchPage import SearchPage


@pytest.fixture(scope="function")
def page(driver):
    return SearchPage(driver)


@pytest.mark.smoke
def test_in_stock_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    if page.in_stock_filter_ON.is_presented():
        assert page.in_stock_filter_ON.is_presented()
    else:
        page.availability_filters.click()
        page.in_stock_filter.click()
        page.accept_availability_filters.wait_to_be_clickable()
        page.accept_availability_filters.click()
        page.in_stock_filter_ON.wait_to_be_clickable()
        assert page.in_stock_filter_ON.is_presented()


def test_expeсted_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    if page.expected_filter_ON.is_presented():
        assert page.expected_filter_ON.is_presented()
    else:
        page.availability_filters.click()
        page.expected_filter.click()
        page.accept_availability_filters.wait_to_be_clickable()
        page.accept_availability_filters.click()
        page.expected_filter_ON.wait_to_be_clickable()
        assert page.expected_filter_ON.is_presented()


def test_pre_order_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    if page.pre_order_filter_ON.is_presented():
        assert page.pre_order_filter_ON.is_presented()
    else:
        page.availability_filters.click()
        page.pre_order_filter.click()
        page.accept_availability_filters.wait_to_be_clickable()
        page.accept_availability_filters.click()
        page.pre_order_filter_ON.wait_to_be_clickable()
        assert page.pre_order_filter_ON.is_presented()


def test_not_on_sale_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    if page.not_on_sale_filter_ON.is_presented():
        assert page.not_on_sale_filter_ON.is_presented()
    else:
        page.availability_filters.click()
        page.not_on_sale_filter.click()
        page.accept_availability_filters.wait_to_be_clickable()
        page.accept_availability_filters.click()
        page.not_on_sale_filter_ON.wait_to_be_clickable()
        assert page.not_on_sale_filter_ON.is_presented()


@pytest.mark.parametrize('min, max', [(1000, 2000), (2550, 3000), (5000, 6000)])
def test_price_filter_work(driver, page, min, max):
    page.filtered_field.scroll_to_element()
    page.price_filters.click()
    page.price_min = min
    page.price_max = max
    page.accept_price_filters.wait_to_be_clickable()
    page.accept_price_filters.click()
    page.wait_page_loaded(10)
    for price in page.product_prices.get_text():
        assert min <= int(price.replace(' ','')) <= max


@pytest.mark.smoke
def test_fiction_genre_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    page.genre_filters.click()
    page.wait_page_loaded()
    page.fiction.click()
    page.classical_prose.click()
    page.all_classical_prose.click()
    page.wait_page_loaded()
    for genre in page.product_cards.get_attribute('data-first-genre-name'):
        assert genre == 'Художественная литература'


def test_publisher_filter_work(driver, page):
    page.filtered_field.scroll_to_element()
    page.all_filters.click()
    page.wait_page_loaded()
    page.publishers.click()
    page.publisher_AST.click()
    page.accept_all_filters.click()
    page.wait_page_loaded()
    for genre in page.product_cards.get_attribute('data-pubhouse'):
        assert genre == 'АСТ'