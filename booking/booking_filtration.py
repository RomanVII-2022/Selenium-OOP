from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def apply_star_rating(self):
       star_filtration_boxs = self.driver.find_elements(By. XPATH, "//div[@data-filters-group='class']/div/label/span[2]")
       for i in range(2,5):
        star_filtration_boxs[i].click()