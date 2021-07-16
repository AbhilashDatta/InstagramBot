from selenium import webdriver
from time import sleep
import pyperclip as pc
from credentials import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from __login__ import Login
from __logout__ import Logout
from __dm__ import Dm
from __multiple_dm__ import Multiple_dm
from __group_dm__ import Group_dm
from __retrieve_message__ import Retrieve_message


class Bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def login(self, usrname, passkey):
        Login(self.driver, usrname, passkey)

    def logout(self):
        Logout(self.driver)

    def dm(self, user,message):
        Dm(self.driver, user, message)
        self.driver.get('https://www.instagram.com/')

    def multiple_dm(self, users, message):
        Multiple_dm(self.driver, users, message)
        self.driver.get('https://www.instagram.com/')

    def group_dm(self, users, message):
        Group_dm(self.driver, users, message)
        self.driver.get('https://www.instagram.com/')

    def retrieve_message(self, user):
        Retrieve_message(self.driver,user)
        self.driver.get('https://www.instagram.com/')
    

if __name__ == '__main__':
    bot = Bot()
    bot.login('abhilash.datta', '8224abhi')
    bot.retrieve_message('nyctophile')
    bot.retrieve_message('testaccount')
    bot.retrieve_message('kartik_murthy')

    bot.logout()
