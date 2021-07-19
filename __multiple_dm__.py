from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from __dm__ import Dm

def Multiple_dm(driver,users,message):
    ''' This function sends a message to multiple users individually '''
    if isinstance(users,str):
        users = [users]

    for user in users:
        Dm(driver, user, message)
        