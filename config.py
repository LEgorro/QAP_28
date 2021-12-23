import random
import string

url_main_page = 'https://www.labirint.ru'
url_auth = 'https://www.labirint.ru/cabinet/'
user_code = 'BCAE-42BF-9F25'


def gen_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string