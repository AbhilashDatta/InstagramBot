from selenium import webdriver
from time import sleep
import pyperclip as pc
import pyautogui as pt

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def Retrieve_message(driver, user):
    ''' Function to retrieve the latest message of a specified user '''

    search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
    search_user.send_keys(user)

    userclick = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div'))).click()
    
    m_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button'))).click()
    
    wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
    
    # move to latest message

    smily = pt.locateOnScreen('images/insta_smily.jpg', confidence = 0.9)
    pt.moveTo(smily[0:2], duration = 0.5)
    pt.moveRel(70, -70, duration = 0.5)

    dots = pt.locateOnScreen('images/insta_dots.png', confidence = 0.9)
    pt.moveTo(dots[0:2], duration = 0.5)
    pt.click()

    copy = pt.locateOnScreen('images/insta_copy.jpg', confidence = 0.9)
    pt.moveTo(copy[0:2], duration = 0.5)
    pt.click()

    message = pc.paste()
    full_message = user+' : '+message+'\n'

    with open('Retrieved_messages.txt', 'a') as f:
        f.write(full_message)