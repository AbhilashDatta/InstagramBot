from selenium import webdriver
from time import sleep
import pymongo
from pymongo import MongoClient
from db_credentials import username as db_username
from db_credentials import password as db_password
from credentials import username as ig_username
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def Share_latest_post(driver):    

    # search for latest post
    profile = 'https://www.instagram.com/' + ig_username

    driver.get(profile)

    links = driver.find_elements_by_tag_name('a')

    def condition(link):
        return 'https://www.instagram.com/p/' in link.get_attribute('href')

    valid_links = list(filter(condition, links))

    latest_post_link = valid_links[0].get_attribute('href')
    driver.get(latest_post_link)

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')))
    
    texts = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span')
    
    caption = str(texts[0])

    political = 0
    social = 0
    activism = 0
    history = 0 

    category = []

    if caption.find('political'):
        political = 1
        category.append('political')
        print('Political post')

    if caption.find('social'):
        social = 1
        category.append('social')
        print('Social post')
    
    if caption.find('activism'):
        activism = 1
        category.append('activism')
        print('Activism post')

    if caption.find('history'):
        history = 1
        category.append('history')
        print('History post')


    user_list = []

    url = "mongodb+srv://"+db_username+":"+db_password+"@cluster0.rboro.mongodb.net/Retrieved_Messages?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client['Retrieved_Messages']
    collection = db['Messages']
    results = collection.find({})
   
    for result in results:
        result['message']= result['message'].lower()

        if result['message'].find('political')!=-1 and 'political' in category:
            user_list.append(result['username'])

        elif result['message'].find('social')!=-1 and 'social' in category:
            user_list.append(result['username'])

        elif result['message'].find('activism')!=-1 and 'activism' in category:
            user_list.append(result['username'])

        elif result['message'].find('history')!=-1 and 'history' in category:
            user_list.append(result['username'])


    
    share = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[3]/button'))).click()
    
    for user in user_list:
        search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')))
        search_user.send_keys(user)
        selector = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button'))).click()
    
        
    send = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[4]/button/div'))).click()
    