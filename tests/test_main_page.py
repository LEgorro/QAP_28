import pytest

from pages.MainPage import MainPage
from config import gen_random_string


@pytest.mark.smoke
def test_app_is_available(driver):
    page = MainPage(driver)
    assert page.get_title() == 'Лабиринт | Книжный интернет-магазин: купить книги, новинки, бестселлеры'


@pytest.mark.smoke
def test_page_not_found(driver):
    page = MainPage(driver, url=r'https://www.labirint.ru/not_there/')
    assert page.get_title() == 'Ошибка 404. Интернет-магазин Лабиринт.'


def test_is_there_logo(driver):
    page = MainPage(driver)
    assert page.logo.is_presented()


def test_is_there_search_field(driver):
    page = MainPage(driver)
    assert page.search.is_presented()


def test_is_there_messages_button(driver):
    page = MainPage(driver)
    assert page.messages_button.is_presented()


def test_is_there_my_labirint_button(driver):
    page = MainPage(driver)
    assert page.my_labirint_button.is_presented()


def test_is_there_postponed_button(driver):
    page = MainPage(driver)
    assert page.postponed_button.is_presented()


def test_is_there_cart_button(driver):
    page = MainPage(driver)
    assert page.cart_button.is_presented()


def test_is_there_contact_header_button(driver):
    page = MainPage(driver)
    assert page.contact_header_button.is_presented()


def test_is_there_support_header_button(driver):
    page = MainPage(driver)
    assert page.support_header_button.is_presented()


@pytest.mark.smoke
@pytest.mark.parametrize('book_name', ['Снежная королева',
                                       'Обломов',
                                       'Маленькие женщины',
                                       'Чук и Гек',
                                       'Wives and Daughters'])
def test_search_real_book(driver, book_name):
    page = MainPage(driver)
    page.search = book_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if book_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5


def test_empty_search(driver):
    page = MainPage(driver)
    page.search_run_button.click()
    assert driver.title == 'Лабиринт | Книжный интернет-магазин: купить книги, новинки, бестселлеры'


def test_whitespace_search(driver):
    page = MainPage(driver)
    page.search = ' '
    page.search_run_button.click()
    assert page.search_error.is_presented()


def test_abracadabra_search(driver):
    page = MainPage(driver)
    page.search = 'kljnfd;snfgd asqwr'
    page.search_run_button.click()
    assert page.search_error.is_presented()


def test_special_character_search(driver):
    page = MainPage(driver)
    page.search = '[̲̅♥̲̲̅̅l̲̲̅̅i̲̲̅̅t̲̲̅̅t̲̲̅̅l̲̲̅̅e̲̲̅̅ ̲̲̅̅w̲̲̅̅o̲̲̅̅o̲̲̅̅m̲̲̅̅a̲̲̅̅n̲̲̅̅♥̲̅]'
    page.search_run_button.click()
    assert page.search_error.is_presented()


def test_english_search(driver):
    page = MainPage(driver)
    page.search = 'Little Dorrit'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = f'Wrong product in search "{title}"'
        assert 'little dorrit' or 'крошка доррит' in title.lower(), msg


@pytest.mark.parametrize('wrong_book_name, book_name', [('кОпитанская доча', 'капитанская дочка'),
                                                        ('земля саникова', 'земля санникова'),
                                                        ('pfnthzyysq vbh', 'затерянный мир'),
                                                        ('сердца 3х', 'сердца трех'),
                                                        ('метро две тысячи тридцать три', 'метро 2033')])
def test_misspell_search(driver, wrong_book_name, book_name):
    page = MainPage(driver)
    page.search = wrong_book_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    # for title in page.products_titles.get_text()[:int(page.products_titles.count()*0.5)]:
    #     msg = f'Wrong product in search "{title}"'
    #     assert book_name in title.lower(), msg
    relevant_book = 0
    for title in page.products_titles.get_text():
        if book_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5


def test_string_255_search(driver):
    page = MainPage(driver)
    page.search = gen_random_string(255)
    page.search_run_button.click()
    assert page.search_error.is_presented()


def test_string_over9000_search(driver):
    page = MainPage(driver)
    page.search = gen_random_string(9001)
    page.search_run_button.click()
    assert page.search_error.is_presented()


@pytest.mark.parametrize('author_name', ['Пушкин', 'Лондон Джек', 'Гоголь'])
def test_by_author_search(driver, author_name):
    page = MainPage(driver)
    page.search = author_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if author_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.


@pytest.mark.parametrize('publisher_name', ['Эксмо', 'АСТ', 'Вече'])
def test_by_publisher_search(driver, publisher_name):
    page = MainPage(driver)
    page.search = publisher_name
    page.search_run_button.click()
    assert page.book_publisher.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if publisher_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5