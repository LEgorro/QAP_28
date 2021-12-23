import pytest
from config import user_code, gen_random_string
from pages.AuthPage import AuthPage


@pytest.fixture(scope="function")
def page(driver):
    return AuthPage(driver)


@pytest.mark.smoke
def test_auth_with_valid_data(driver, page):
    page.input_field = user_code
    page.enter_button.click()
    page.text_code.wait_until_not_visible()
    assert page.text_code.is_presented()


def test_auth_with_invalid_data(driver, page):
    page.input_field = 'invalid user code'
    page.enter_button.click()
    page.wait_page_loaded()
    assert page.error_code_msg.is_presented()


def test_auth_with_nothing(driver, page):
    page.input_field = ''
    assert page.enter_button.is_clickable() == False


def test_auth_with_whitespaces(driver, page):
    page.input_field = ' '
    assert page.error_whitespaces_msg.is_presented()


def test_auth_with_too_long_phone_number(driver, page):
    page.input_field = '+7123456789012'
    page.enter_button.click()
    page.error_phone_msg.wait_until_not_visible()
    assert page.error_phone_msg.is_presented()


def test_auth_with_special_character(driver, page):
    page.input_field = '@'  # or any another special character
    page.error_wrong_char_msg.wait_until_not_visible()
    assert page.error_wrong_char_msg.is_presented()
    assert page.enter_button.is_clickable() == False


def test_auth_with_cyrillic_character(driver, page):
    page.input_field = 'кирилличесие символы'
    page.enter_button.click()
    assert page.error_code_msg.is_presented()


def test_auth_with_china_character(driver, page):
    page.input_field = '空格'
    page.error_wrong_char_msg.wait_until_not_visible()
    assert page.error_wrong_char_msg.is_presented()
    assert page.enter_button.is_clickable() == False


def test_auth_with_string_255(driver, page):
    page.input_field = gen_random_string(255)
    page.enter_button.click()
    assert page.error_code_msg.is_presented()


def test_auth_with_string_over1000(driver, page):
    page.input_field = gen_random_string(1001)
    page.enter_button.click()
    page.error_code_msg.wait_until_not_visible()
    assert page.error_code_msg.is_presented()


@pytest.mark.smoke
def test_registration(driver, page):
    page.input_field = gen_random_string(5) + '@' + gen_random_string(3) + '.com'
    page.enter_button.click()
    page.text_code.wait_until_not_visible()
    assert page.text_code.is_presented()


def test_logout(driver_with_cookies, page):
    if page.coupon_reminder.is_visible():
        page.my_labirint_button.click()
    page.my_labirint_button.move_to_show_submenu()
    page.logout_button.click()