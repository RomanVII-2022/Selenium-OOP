from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from booking.constants import BASE_URL
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.filtration_info import FiltrationInfo


class Booking:
    def __init__(self, driver=webdriver.Chrome(service=Service("C:\Program Files (x86)\chromedriver.exe")), teardown=True):
        self.driver = driver 
        self.teardown = teardown
        super(Booking, self).__init__()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def __enter__(self):
        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()



    def land_page(self):
        self.driver.get(BASE_URL)



    def change_currency(self, currency):
        self.driver.find_element(By.XPATH, "//header[contains(@class,'bui-header bui-header--logo-large bui-u-hidden-print bui-header--rounded-tabs')]//div[1]//button[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, f"a[data-modal-header-async-url-param='changed_currency=1&selected_currency={currency}']").click()



    def place_to_go(self, place_go):
        place = self.driver.find_element(
            By.XPATH, "//input[@id='ss']"
        )
        place.clear()
        place.send_keys(place_go)
        place_dropdown = self.driver.find_element(
            By.XPATH, "//ul[@aria-label='List of suggested destinations ']/li[1]"
        )
        place_dropdown.click()



    def check_in_and_check_out(self, check_in_date, check_in_day, check_out_date, check_out_day):
        check_in_month_and_year = check_in_date
        check_out_month_and_year = check_out_date

        while True:
            check_in = self.driver.find_element(
                By.XPATH, "//form[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//div[1]"
                )
            if check_in.text == check_in_month_and_year:
                break
            else:
                next = self.driver.find_element(
                    By.XPATH, "//div[@class='bui-calendar__control bui-calendar__control--next']"
                    )
                next.click()

        dates = self.driver.find_elements(
            By.XPATH, "//table[@class='bui-calendar__dates']/tbody//td"
            )
        for date in dates:
            if date.text == check_in_day:
                date.click()
                break

        
        while True:
            check_out = self.driver.find_element(
                By.XPATH, "//form[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//div[1]"
                )
            if check_out.text == check_out_month_and_year:
                break
            else:
                next = self.driver.find_element(
                    By.XPATH, "//div[@class='bui-calendar__control bui-calendar__control--next']"
                    )
                next.click()

        dates = self.driver.find_elements(
            By.XPATH, "//table[@class='bui-calendar__dates']/tbody//td"
            )
        for date in dates:
            if date.text == check_out_day:
                date.click()
                break 


    def number_of_adults(self):
        adult_input = self.driver.find_element(
            By.XPATH, "//div[@class='xp__input-group xp__guests']"
            )
        adult_input.click()

        add_button = self.driver.find_element(
            By.XPATH, "//button[@aria-label='Increase number of Adults']"
            )
        add_button.click()

    
    def search_button(self):
        search = self.driver.find_element(By.XPATH, "//button[@class='sb-searchbox__button ']")
        search.click()


    def pop_up(self):
        close_button = self.driver.find_element(By.XPATH, "//div[@aria-label='Close map']")
        close_button.click()


    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self.driver)
        filtration.apply_star_rating()


    def fiitration_information(self):
        hotel_information = FiltrationInfo(driver=self.driver)
        hotel_information.get_hotel_details()
        hotel_information.pull_title()