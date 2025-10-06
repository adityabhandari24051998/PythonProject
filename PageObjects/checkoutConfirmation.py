import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckConfirm:
    def __init__(self,driver):
        self.driver=driver
        self.clickCheck = (By.XPATH, "//button[@class='btn btn-success']")
        self.deliveryLocation = (By.XPATH, "//input[@id='country']")
        self.clickCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def checkConf(self):
        # Click on Checkout
        self.driver.find_element(*self.clickCheck).click()
        time.sleep(2)

        # Choose delivery location
    def delivery_address(self):
        self.driver.find_element(*self.deliveryLocation).send_keys("ind")

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()

        # Click on checkbox
        self.driver.find_element(*self.clickCheckbox ).click()

        # Click on purchase
        self.driver.find_element(*self.purchase).click()

    def delivery_confirmation(self):
        success_text = self.driver.find_element(*self.success).text

        assert "Success" in success_text