from selenium import webdriver
from time import sleep
import pyperclip as pc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from __login__ import Login
from __logout__ import Logout
from __dm__ import Dm
from __multiple_dm__ import Multiple_dm
from __group_dm__ import Group_dm
from __retrieve_messages__ import Retrieve_messages
from __follow_users__ import Follow_users
from __download_pics__ import Download_pics
from __like_by_keyword__ import Like_by_keyword
from __multiple_dm_from_csv__ import Multiple_dm_from_csv
from __retrieve_messages_from_csv__ import Retrieve_messages_from_csv
from __multiple_dm_from_db__ import Multiple_dm_from_db
from __retrieve_messages_from_inbox__ import Retrieve_messages_from_inbox
from __multiple_dm_followers__ import Multiple_dm_followers
from __share_latest_post__ import Share_latest_post

class Bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def login(self, usrname, passkey):
        try:
            Login(self.driver, usrname, passkey)
        except:
            print("Unable to Login!")
            exit(0)

    def logout(self):
        Logout(self.driver)
        self.driver.minimize_window()

    def dm(self, user,message):
        try:
            Dm(self.driver, user, message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to DM!")
            self.driver.get('https://www.instagram.com/')

    def multiple_dm(self, users, message):
        try:
            Multiple_dm(self.driver, users, message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to DM!")
            self.driver.get('https://www.instagram.com/')

    def group_dm(self, users, message):
        try:
            Group_dm(self.driver, users, message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to DM!")
            self.driver.get('https://www.instagram.com/')

    def retrieve_messages(self, users):
        try:
            Retrieve_messages(self.driver,users)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Retrieve message!")
            self.driver.get('https://www.instagram.com/')

    def follow_users(self, users):
        try:
            Follow_users(self.driver, users)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Follow user!")
            self.driver.get('https://www.instagram.com/')

    def download_pics(self, keyword):
        try:
            Download_pics(self.driver, keyword)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Download posts!")
            self.driver.get('https://www.instagram.com/')

    def like_by_keyword(self, keyword, n = 5):
        try:
            Like_by_keyword(self.driver, keyword, n)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Like post!")
            self.driver.get('https://www.instagram.com/')

    def multiple_dm_from_csv(self, csv_file, general_message = ''):
        try:
            Multiple_dm_from_csv(self.driver, csv_file, general_message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to send message!")
            self.driver.get('https://www.instagram.com/')

    def retrieve_messages_from_csv(self, csv_file):
        try:
            Retrieve_messages_from_csv(self.driver,csv_file)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Retrieve message!")
            self.driver.get('https://www.instagram.com/')

    def multiple_dm_from_db(self, general_message = ''):
        try:
            Multiple_dm_from_db(self.driver, general_message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to send message!")
            self.driver.get('https://www.instagram.com/')

    def retrieve_messages_from_inbox(self, tolerance = 0):
        try:
            Retrieve_messages_from_inbox(self.driver, tolerance)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to Retrieve message!")
            self.driver.get('https://www.instagram.com/')

    def multiple_dm_followers(self, message):
        try:
            Multiple_dm_followers(self.driver, message)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to send message!")
            self.driver.get('https://www.instagram.com/')

    def share_latest_post(self):
        try:
            Share_latest_post(self.driver)
            self.driver.get('https://www.instagram.com/')
        except:
            print("Unable to send message!")
            self.driver.get('https://www.instagram.com/')