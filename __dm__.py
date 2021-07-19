from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def Dm(driver,user,message):
    ''' This function is used to direct message a single user/group '''

    driver.get('https://www.instagram.com/direct/inbox/')
    
    send_message_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button'))).click()
    
    search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')))
    search_user.send_keys(user)
    
    selector = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span'))).click()
    
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div'))).click()
    
    try:
        text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
        text.send_keys(message)
        send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'))).click()
        driver.get('https://www.instagram.com/direct/inbox/')
    
    except:
        print('No message sent to '+user)
        driver.get('https://www.instagram.com/direct/inbox/')