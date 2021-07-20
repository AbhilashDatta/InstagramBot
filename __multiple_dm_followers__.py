from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from __dm__ import Dm
from credentials import username, password
from __multiple_dm__ import Multiple_dm

def Multiple_dm_followers(driver, message):
    
    profile = 'https://www.instagram.com/'+username

    driver.get(profile)

    followerclick = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
        
    i = 1
    users = []

    while True:

        xpath = '/html/body/div[5]/div/div/div[2]/ul/div/li[' +str(i)+']/div/div[2]/div[1]/div/div/span/a'
        i += 1

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            user = driver.find_element_by_xpath(xpath).text
            users.append(user)

        except:
            # print(users)
            driver.get('https://www.instagram.com/')
            Multiple_dm(driver, users, message)
            break