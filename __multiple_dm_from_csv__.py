from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from __dm__ import Dm

def Multiple_dm_from_csv(driver, csv_file, general_message = ''):
    ''' This function sends a message to multiple users from a csv file '''
    '''
        csv_file should have columns like-
        users   message 
        user1   msg1
        user2   msg2
        ..     .. 

        OR 
        users    
        user1   
        user2   
        ..
    '''

    df = pd.read_csv(csv_file)

    if 'message' in df.columns:
        for i in range(len(df)):
            user = df.iloc[i]['users']
            message = df.iloc[i]['message']

            Dm(driver, user, message)
    
    else:
        for i in range(len(df)):
            user = df.iloc[i]['users']

            Dm(driver, user, general_message)
        