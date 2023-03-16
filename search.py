from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, json


def initial_webdriver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    wait = WebDriverWait(browser, 5)
    return (browser, wait)

def find_channel(browser, wait, user_input):
    browser.get(url='http://www.youtube.com')
    input_bar = browser.find_element(By.NAME, 'search_query')
    input_bar.send_keys(user_input)
    input_bar.submit()
    
    wait.until(EC.presence_of_element_located((By.ID, 'content-section')))
    browser.find_element(By.ID, 'content-section').click()
    
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')))
    browser.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click()
    time.sleep(0.5)
    
def scroll_window(browser):
    last_height = browser.execute_script("return document.documentElement.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(0.5)
        new_height = browser.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    browser.find_element(By.TAG_NAME,'html').send_keys(Keys.HOME)   
    time.sleep(0.5)
    
def get_data(browser):
    data = []
    information = browser.find_elements(By.ID, 'video-title-link')
    for i in information: 
        link = i.get_attribute('href')
        try:
            i.click()
        except Exception:
            continue
        time.sleep(1)
        data.append(
            {
            'Name':browser.find_element(By.XPATH,'//*[@id="title"]/h1/yt-formatted-string').text, 
            'Link': link,
            'Number of views': browser.find_element(By.XPATH,'//*[@id="info"]/span[1]').text,
            'Likes':browser.find_element(By.XPATH, '//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/div[2]/span').text,
            'Upload date':browser.find_element(By.XPATH,'//*[@id="info"]/span[3]').text
            }
        )
        browser.back()
        browser.find_element(By.TAG_NAME,'html').send_keys(Keys.HOME) 
        time.sleep(1)
    return data
    
def save_data(data):
    with open('last_video.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    user_input = input('Еnter the channel name: ')
    
    browser, wait = initial_webdriver()
    find_channel(browser, wait, user_input)
    scroll_window(browser)
    data = get_data(browser)
    save_data(data)
    
    browser.close()
    browser.quit()
    
if __name__ == '__main__':
    main()
    
