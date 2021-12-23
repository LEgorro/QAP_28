import pytest
from pages.ContactPage import ContactPage


@pytest.fixture(scope="function")
def page(driver):
    return ContactPage(driver)


@pytest.mark.smoke
def test_connect_with_operator_button__on_page(driver, page):
    assert page.connect_with_the_operator_button.is_presented()


def test_support_phone_number_on_page(driver, page):
    assert page.phone_number.is_presented()


def test_support_email_on_page(driver, page):
    assert page.e_mail.is_presented()