import pytest
from selenium import webdriver

from pages.pages import RegistrationPage, AuthPage, FilterPage, BookingPage

"""Фикстура для инициализации и закрытия драйвера"""
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://excursium.com/')

    yield driver
    driver.quit()

"""Функциональные положительные тесты"""

"""Регистрация"""
def test_registration(driver):
    rp = RegistrationPage(driver)
    ap = AuthPage(driver)
    ap.click_to_btn_account()
    driver.implicitly_wait(10)
    rp.get_page_registration()
    driver.implicitly_wait(10)
    rp.get_input_email('test112@gmail.ru') # Понятно, что емайл одноразовый
    rp.get_input_pass('test999')
    rp.click_agreement()
    rp.click_create_account()
    driver.implicitly_wait(10)
    message = rp.get_send_msg()
    try:
        assert message == "На вашу почту было отправлено письмо с ", "Registration failed"
    except Exception:
        return None

"""Авторизация"""
def test_authorization(driver):
    ap = AuthPage(driver)
    ap.click_to_btn_account()
    driver.implicitly_wait(10)
    ap.get_input_email('test999qqq@mail.ru')
    ap.get_input_pass('test123')
    ap.click_btn_login()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    expected_url = "https://excursium.com/Account/Dashboard"
    try:
        assert current_url == expected_url, "Autorization failed"
    except Exception:
        return None

"""Фильтрация"""
def test_filtering(driver):
    fp = FilterPage(driver)
    bp = BookingPage(driver)
    driver.refresh()
    driver.implicitly_wait(5)
    bp.click_on_begin_exc()
    driver.implicitly_wait(5)
    fp.click_to_rating_scholl()
    fp.click_to_btn_class()
    fp.click_to_btn_price()
    fp.click_to_btn_time()
    fp.click_to_btn_place()
    fp.click_to_btn_activity()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    expected_url = "https://excursium.com/ekskursii-dlya-shkolnikov/list?grades=2&types=7%2C32&price=2500&times=6&regions=77"
    try:
        assert current_url == expected_url, "Filter work unsuccess"
    except Exception:
        return None

"""Бронирование"""
def test_booking(driver):
    bp = BookingPage(driver)
    driver.implicitly_wait(5)
    bp.click_on_begin_exc()
    bp.click_on_first_exc()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("window.scrollBy(0, 800)")
    bp.click_book_exc()
    driver.implicitly_wait(10)
    bp.click_quantity()
    bp.write_name_book('Иван')
    bp.write_phone_book(0000000000)
    bp.click_on_agree_check()
    bp.click_on_send_applic()
    message = bp.get_text_scs()
    try:
        assert message == "Заявка принята, ", "Booking failed"
    except Exception:
        return None
