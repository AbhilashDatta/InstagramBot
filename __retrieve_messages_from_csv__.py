from selenium import webdriver
from time import sleep
import pyperclip as pc
import pyautogui as pt
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from __retrieve_messages__ import Retrieve_messages


def Retrieve_messages_from_csv(driver, csv_file):
    ''' Function to retrieve the latest message of users specified in a csv file '''
    '''
        csv_file should have the following column:
        users
        user1
        user2
        ..
    '''
    df = pd.read_csv(csv_file)

    user_list = df['users'].tolist()

    Retrieve_messages(driver,user_list)