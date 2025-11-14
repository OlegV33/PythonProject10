from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open(self, url):
        self.driver.get(self. url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.find(locator).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def scroll_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)


class RegistrationPage(BasePage):
    LOCATOR_CREATE_ON_ACCOUNT = (By.XPATH, '//*[@id=\"login-vue\"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]/a[1]')
    LOCATOR_BTN_AGREEMENT = (By.XPATH, '//*[@id=\"agreement-block\"]/label[1]')
    LOCATOR_BTN_CREATE = (By.ID, "registraion-btn")
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[2]/div[1]/input')
    LOCATOR_FIELD_PASS = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[2]/div[2]/input')
    LOCATOR_TEXT_MSG = (By.XPATH, "//*[contains(text(), 'На вашу почту было отправлено письмо с ')]")

    def get_page_registration(self):
        self.find(self.LOCATOR_CREATE_ON_ACCOUNT).click()

    def get_input_email(self, email_value):
        self.find(self.LOCATOR_FIELD_EMAIL).send_keys(email_value)

    def get_input_pass(self, password_value):
        self.find(self.LOCATOR_FIELD_PASS).send_keys(password_value)

    def click_agreement(self):
        self.find(self.LOCATOR_BTN_AGREEMENT).click()

    def click_create_account(self):
        self.find(self.LOCATOR_BTN_CREATE).click()

    def get_send_msg(self):
        return self.get_text(self.LOCATOR_TEXT_MSG)


class AuthPage(BasePage):
    LOCATOR_BTN_ACCOUNT = (By.XPATH, '//a[@href=\"/Client/Login\"]')
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[1]/div[1]/input')
    LOCATOR_FIELD_PASS = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[1]/div[2]/input')
    LOCATOR_BTN_LOGIN = (By.ID, "login-btn")

    def click_to_btn_account(self):
        #self.open(self. 'https://excursium.com/')
        self.find(self.LOCATOR_BTN_ACCOUNT).click()

    def get_input_email(self, email_value):
        self.find(self.LOCATOR_FIELD_EMAIL).send_keys(email_value)

    def get_input_pass(self, password_value):
        self.find(self.LOCATOR_FIELD_PASS).send_keys(password_value)

    def click_btn_login(self):
        self.find(self.LOCATOR_BTN_LOGIN).click()


class FilterPage(BasePage):
    LOCATOR_BTN_RATING_SCHOOLL = (By.XPATH, '//*[@id=\"popolarType_7\"]')
    LOCATOR_BTN_CLASS_2 = (By.XPATH, '//*[@id=\"collapse-grade\"]/li[2]/label')
    LOCATOR_BTN_PRICE_2500 = (By.ID, 'priceRange_2500')
    LOCATOR_BTN_TIME_1 = (By.ID, 'time_6')
    LOCATOR_BTN_PLACE_MOSCOW = (By.ID, 'regions_77')
    LOCATOR_BTN_ACTIVITY = (By.ID, 'activity3232')
    LOCATOR_BTN_CLEAR = (By.XPATH, '//*[@id=\"offcanvasSidebar\"]/div[3]/button')

    def click_to_rating_scholl(self):
        self.find(self.LOCATOR_BTN_RATING_SCHOOLL).click()

    def click_to_btn_class(self):
        self.scroll_and_click(self.LOCATOR_BTN_CLASS_2)

    def click_to_btn_price(self):
        self.scroll_and_click(self.LOCATOR_BTN_PRICE_2500)

    def click_to_btn_time(self):
        self.scroll_and_click(self.LOCATOR_BTN_TIME_1)

    def click_to_btn_place(self):
        self.scroll_and_click(self.LOCATOR_BTN_PLACE_MOSCOW)

    def click_to_btn_activity(self):
        self.scroll_and_click(self.LOCATOR_BTN_ACTIVITY)

    def click_to_filter_clear(self):
        self.scroll_and_click(self.LOCATOR_BTN_CLEAR)


class BookingPage(BasePage):
    LOCATOR_BTN_BEGIN = (By.XPATH, '/html/body/main/div/section/div/div[1]/div[1]/div/a')
    LOCATOR_FIRST_EXC = (By.XPATH, '//*[@id=\"excursion-vue\"]/section[2]/div/div/div/div/div[2]/div[19]/div/div[4]/div/div[2]/button')
    LOCATOR_BTN_BOOK = (By.XPATH, '//*[@id=\"detail-vue\"]/section[3]/div/div/div[2]/div/div/div/div[5]/button')
    LOCATOR_BTN_QUANTITY = (By.XPATH, '//*[@id=\"bookingModal\"]/div/div/div[2]/div[1]/div/label[1]')
    LOCATOR_FIELD_NAME = (By.ID, "bookingUserName")
    LOCATOR_FIELD_PHONE = (By.ID, "orderPhone")
    LOCATOR_BTN_AGREE_CHECK =(By.XPATH, '//*[@id=\"bookingModal\"]/div[1]/div[1]/div[2]/div[7]/label[1]')
    LOCATOR_SEND_APPLIC = (By.XPATH, '//*[@id=\"bookingModal\"]/div[1]/div[1]/div[3]')
    LOCATOR_TEXT_SCS = (By.XPATH, '//*[@id=\"bookingSuccess\"]/div/div/div/p')

    def click_on_begin_exc(self):
        self.find(self.LOCATOR_BTN_BEGIN).click()

    def click_on_first_exc(self):
        self.scroll_and_click(self.LOCATOR_FIRST_EXC)

    def click_book_exc(self):
        self.scroll_and_click(self.LOCATOR_BTN_BOOK)

    def click_quantity(self):
        self.find(self.LOCATOR_BTN_QUANTITY).click()

    def write_name_book(self, name_value):
        self.find(self.LOCATOR_FIELD_NAME).send_keys(name_value)

    def write_phone_book(self, phone_value):
        self.find(self.LOCATOR_FIELD_PHONE).send_keys(phone_value)

    def click_on_agree_check(self):
        self.find(self.LOCATOR_BTN_AGREE_CHECK).click()

    def click_on_send_applic(self):
        self.find(self.LOCATOR_SEND_APPLIC).click()

    def get_text_scs(self):
        return self.get_text(self.LOCATOR_TEXT_SCS)
