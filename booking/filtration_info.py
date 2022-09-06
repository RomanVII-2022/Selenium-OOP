from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class FiltrationInfo:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.deal_boxes = self.get_hotel_details()


    def get_hotel_details(self):
       return self.driver.find_elements(By.XPATH, "//div[@class='d4924c9e74']/div[@data-testid='property-card']")


    def pull_title(self):
        all = []
        for box in self.deal_boxes:
            hotel_name = box.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text  
            hotel_price = box.find_element(By.CSS_SELECTOR, "[data-testid='price-and-discounted-price']").text
            all.append([hotel_name, hotel_price])

        table = PrettyTable(["Hotel Name", "Hotel Price"])
        table.add_rows(all)
        print(table)
            
           
        


