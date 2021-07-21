from selenium import webdriver
from time import sleep
import pyperclip as pc
import pyautogui as pt
import pymongo
from pymongo import MongoClient
from db_credentials import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def Retrieve_messages_from_inbox(driver, tolerance = 0):
    ''' Function to retrieve the latest messages from inbox '''

    url = "mongodb+srv://"+username+":"+password+"@cluster0.rboro.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(url)
    db = client['Retrieved_Messages']
    collection = db['Messages']
    # collection.delete_many({})
    i = 1
    tol = 0

    while True:
        driver.get('https://www.instagram.com/direct/inbox/')

        xpath = '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div['+str(i)+']/a/div/div[3]/div'
        i += 1 

        try:
            userclick = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            
        except:
            if tol<tolerance:
                tol += 1
                continue
            
            else:
                break

        
        wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
        
        # move to latest message

        smily = pt.locateOnScreen('images/insta_smily.jpg', confidence = 0.9)
        pt.moveTo(smily[0:2], duration = 0.1)
        pt.moveRel(70, -70, duration = 0.3)
        
        dots = pt.locateOnScreen('images/insta_dots.png', confidence = 0.9)

        try:
            pt.moveTo(dots[0:2], duration = 0.2)
            pt.click()

        except:
            print("No message received from "+user)
            driver.get('https://www.instagram.com/')
            continue

        sleep(1)

        try:
            unsend = pt.locateOnScreen('images/insta_unsend.png', confidence = 0.9)
            pt.moveTo(unsend[0:2],duration = 0.1)
            print('No message received from '+user)
            continue

        except:
            copy = pt.locateOnScreen('images/insta_copy.jpg', confidence = 0.9)
            
            try:
                pt.moveTo(copy[0:2], duration = 0.1)
                pt.click()

            except:
                print("Not a text message from "+user)
                driver.get('https://www.instagram.com/')
                continue


            message = pc.paste()

            user = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div[1]/div').text 

            if collection.find_one({'username':user})!=None:
                res = collection.find_one({'username':user})
                new_message = message+" "+res['message']
                collection.update_one({'username':user}, {"$set":{'message':new_message}})
                continue

            post = {'username':user,'message':message,'last_post_link':'none'}
            collection.insert_one(post)
        

            ''' uncomment the below code to save the messages in a text file '''
            # full_message = user+' : '+message+'\n'

            # with open('Retrieved_messages.txt', 'a') as f:
            #     f.write(full_message)

    
    driver.get('https://www.instagram.com/')

    # print(collection.count_documents({}), " messages retrieved")
    