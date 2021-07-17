from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def Like_by_keyword(driver, keyword, num):
    post_links = []

    search_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
    search_user.send_keys(keyword)

    userclick = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div'))).click()

    if keyword.startswith('#'): 
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')))
    
    else:
        sleep(5)
        
    links = driver.find_elements_by_tag_name('a')

    def condition(link):
        return 'https://www.instagram.com/p/' in link.get_attribute('href')

    valid_links = list(filter(condition, links))

    for i in range(num):
        link = valid_links[i].get_attribute('href')
        if link not in post_links:
            post_links.append(link)
        
        if i==len(valid_links)-1:
            break

    for link in post_links:
        driver.get(link)
        # like
        like = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button'))).click()
