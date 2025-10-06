from selenium.webdriver.common.by import By

class ShopPage:

    def __init__(self,driver):
        self.driver=driver
        self.click_on_shop = (By.XPATH, "//a[text()='Shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")

    def shopping(self,productName):
        # Click on Shop
        self.driver.find_element(*self.click_on_shop).click()

        # Iterating through the list
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == productName:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):

        self.checkout_click = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
        # Click on Checkout
        self.driver.find_element(*self.checkout_click).click()