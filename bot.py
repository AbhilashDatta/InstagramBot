from selenium import webdriver
from time import sleep
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

class Bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        Login(self.driver)

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
    

if __name__ == '__main__':
    bot = Bot()
    bot.login()
    bot.group_dm(['abhilash','kartik'],"hi there, this is an automated message but I'm surely real")
    bot.logout()
