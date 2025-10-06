import json
import pytest
from pycparser.plyparser import parameterized
from selenium import webdriver
import time



from PageObjects.Login import LoginPage
from PageObjects.checkoutConfirmation import CheckConfirm
from PageObjects.shopPage import ShopPage

test_data_path = "./Data/test_end2endFramework.json"
with open(test_data_path)as f:
    test_data = json.load(f)
    test_list= test_data["data"]

@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance



    loginPage = LoginPage(driver)
    loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    time.sleep(5)

    shoPage = ShopPage(driver)
    shoPage.shopping(test_list_item["productName"])
    shoPage.goToCart()


    checkPage = CheckConfirm(driver)
    checkPage.checkConf()
    checkPage.delivery_address()
    checkPage.delivery_confirmation()