import pytest
from pages.CheckoutPage import CheckoutPage


@pytest.fixture(scope="function")
def page(driver_with_cookies):
    page = CheckoutPage(driver_with_cookies)
    page.initializing_checkout_button.click()
    return page

@pytest.mark.smoke
@pytest.mark.parametrize('city', ['Санкт-Петербург', 'Ярославль', 'Казань'],
                         ids=['Sankt-Peterburg', 'Yaroslavl', 'Kazan'])
def test_change_region_post(driver_with_cookies, page, city):
    page.change_region_post_button.click()
    page.input_region_post_field = city
    page.hint_for_region.click()
    page.wait_page_loaded()
    assert page.change_region_post_button.get_text() == city


@pytest.mark.smoke
def test_change_pickup_point(driver_with_cookies, page):
    page.wait_page_loaded()
    if page.pickup_button.is_clickable():
        page.pickup_button.click()
    else:
        page.pickup_change_button.click()
    page.input_point_address_field = 'Арбатская'
    picked_address = page.first_pickup_point_address.get_text()
    page.first_pickup_point.click()
    page.pickup_here.click()
    final_address = page.final_address.get_text()
    assert final_address[:len(final_address)-9:] in picked_address


def test_type_payment(driver_with_cookies, page):
    if page.prepaid_button.is_presented():
        page.prepaid_button.click()
        assert page.prepaid_checked_button.is_presented()
    else:
        page.cash_button.click()
        assert page.cash_chechked_button.is_presented()
    assert page.payment_type_chosen.is_presented()


def test_notification_button(driver_with_cookies, page):
    if page.notification_button_OFF.is_presented():
        page.notification_button_ON.click()
        assert page.notification_button_OFF.is_presented()
    else:
        page.notification_button_ON.click()
        assert page.notification_button_OFF.is_presented()