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
from __follow_user__ import Follow_user
from __download_pics__ import Download_pics


class Bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def login(self, usrname, passkey):
        Login(self.driver, usrname, passkey)

    def logout(self):
        Logout(self.driver)
        self.driver.minimize_window()

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

    def follow_user(self, user):
        Follow_user(self.driver, user)
        self.driver.get('https://www.instagram.com/')

    def download_pics(self, keyword):
        Download_pics(self.driver, keyword)
        self.driver.get('https://www.instagram.com/')
    

if __name__ == '__main__':
    bot = Bot()
    bot.login(username, password)
    bot.download_pics('#dog')
    bot.logout()
