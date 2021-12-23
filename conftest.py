import pytest
import requests

from selenium import webdriver
from config import url_main_page, user_code


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge(r'D:\PycharmProjects\msedgedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='function')
def driver_with_cookies(driver):
    response = requests.post(url=f'{url_main_page}/post.php',
                             data={'post_cl_name': 'authorization',
                                   'post_me_name': 'login',
                                   'code': user_code,
                                   '_jqpostrand': '0'
                                   })
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    driver.get(url_main_page)
    cookie_list = response.request.headers.get('Cookie').split('; ')

    for cookie in cookie_list:
        driver.add_cookie({"name": cookie.split('=')[0], "value": cookie.split('=')[1]})

    yield driver


