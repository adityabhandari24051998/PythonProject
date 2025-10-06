from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_input = (By.XPATH, "//input[@id='username']")
        self.password =(By.XPATH, "//input[@id='password']")
        self.signInButton = (By.XPATH, "//input[@id='signInBtn']")


    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)

        self.driver.find_element(*self.password).send_keys(password)

        self.driver.find_element(*self.signInButton).click()