import os
import time
from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


if __name__ == '__main__':
    fileList = []
    for root, dirs, files in os.walk(os.path.abspath("C:\\Users\\jojop\\Desktop\\AI Convert\\IN\\")):
        for file in files:
            fileList.append(os.path.join(root, file)) #Appends all of the files into the fileList list.
    fileList.sort(key = lambda x: os.path.getmtime(x)) #Sorts the fileList based on the time it was added to the new folder.

###########################################################################################################
def browser_init(aiImageName):
    global driver
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = { 'browser':'ALL' }
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : f'C:\\Users\\jojop\\Desktop\\AI Convert\\OUT\\'}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromeOptions.add_argument("--headless")
    chromedriver = "C:\\Users\\jojop\\Desktop\\AI Convert\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions,desired_capabilities=d)
    driver.get("http://gaugan.org/gaugan2/")
    driver.refresh()
    driver.find_element_by_xpath("//*[@id='myCheck']").click()
    os.chdir("C:\\Users\\jojop\\Desktop\\AI Convert\\OUT\\")

###########################################################################################################
def convert_AI(aiPic, aiImageName):
    element2 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "segmapfile")))
    element2.send_keys(f'C:\\Users\\jojop\\Desktop\\AI Convert\\IN\\{aiImageName}.png')
    element2 = driver.find_element_by_xpath("//*[@id='btnSegmapLoad']")
    element2.send_keys(Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="btnSegmapLoad"]').click()

    element = driver.find_element_by_xpath('//*[@id="example1"]')
    element.click()

    #SEVERE
    time.sleep(3)
    
    print("clicked")
    entry = driver.get_log('browser')[-1]
    val = list(entry.values())[0]
    if val  == "SEVERE":
        print("SEVERE...    RETRYING")
        driver.close()
        browser_init(aiImageName)
        convert_AI(aiPic, aiImageName)
    else:
        print("SUCCESS")
        driver.find_element_by_xpath('//*[@id="save_render"]').click()
        time.sleep(.2)
        os.rename("gaugan_output.jpg", f'{aiImageName}.jpg')

###########################################################################################################
timelist = []
total_len = len(fileList)
for i, file in enumerate(fileList):
    if(i < 393):
        pass
    else:
        browser_init(i)
        old = time.time()
        convert_AI(fileList, i)
        new = time.time()
        timepp = round(new - old)
        timelist.append(timepp)
        avg = sum(timelist)/len(timelist)
        if len(timelist) == 100:
            timelist.pop(0)
        time_remaining = avg * (total_len-i)
        #os.system("cls")
        print(f'Saved Image {i}\nAVG Time:{avg}\nTime Remaining (Hr): {time_remaining/3600}')


