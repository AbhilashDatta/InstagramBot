from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def Group_dm(driver,users,message):
    ''' This function first selects users and forms a group then dms in that group '''

    driver.get('https://www.instagram.com/direct/inbox/')

    send_message_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button'))).click()

    for user in users:
        search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')))
        search_user.send_keys(user)

        selector = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span'))).click()
    

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div'))).click()

    text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
    text.send_keys(message)

    send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'))).click()

    driver.get('https://www.instagram.com/direct/inbox/')