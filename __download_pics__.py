from selenium import webdriver
from time import sleep
import os
import wget
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def Download_pics(driver, keyword):
    ''' Function to follow a specified user '''

    search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
    search_user.send_keys(keyword)

    userclick = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div'))).click()
    
    sleep(5)
    # scroll down to scrape more images
    driver.execute_script("window.scrollTo(0, 4000);")

    # target all images on the page
    images = driver.find_elements_by_tag_name('img')
    
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]

    print('Number of scraped images: ', len(images))
    
    # saving to a directory
    path = os.getcwd()
    path = os.path.join(path, keyword)

    #create the directory
    if(os.path.isdir(path)):
        print('Directory already exists.')
        return
    
    os.mkdir(path)

    #download images
    counter = 0
    for image in images:
        save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

    
