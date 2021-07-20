from selenium import webdriver
from time import sleep
import pandas as pd
import pymongo
from pymongo import MongoClient
from db_credentials import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from __dm__ import Dm

def Multiple_dm_from_db(driver, general_message = ''):
    ''' This function sends a general message to multiple users from a database '''

    url = "mongodb+srv://"+username+":"+password+"@cluster0.rboro.mongodb.net/Retrieved_Messages?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client['Retrieved_Messages']
    collection = db['Messages']
    results = collection.find({})
   
    for result in results:
        Dm(driver, result['username'], general_message)
        # print('Message sent to '+result['username'])