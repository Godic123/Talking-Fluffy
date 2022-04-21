from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getresponse():
    try:
        driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    except:
        driver = webdriver.Chrome("C:\\Users\\Sean\\Documents\\ChromeDriver\\chromedriver.exe")

    driver.get("https://www.eviebot.com/en/")

    try: 
        off = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "suitablenote"))
    
    )

        main = driver.find_element_by_id("suitablenote")
        button = main.find_element_by_class_name("understood")
        button.click()
        time.sleep(0.5)

        textboxmain = driver.find_element_by_id("avatarform")
        textbox = textboxmain.find_element_by_class_name("stimulus")
        
        #/THIS IS THE TEXT I WANT TO SEND
 

        text = open('../STT/speachoutput.txt','r')

        textbox.send_keys(text.read())
        textbox.send_keys(Keys.RETURN)
        time.sleep(5)

        line1 = driver.find_element_by_id("line1")
        print(line1.text)
        with open('../Chatbot/readme.txt', 'w') as f:
            f.write(line1.text)



    finally:
        print("Finished Task")


if __name__ == "__main__":
    getresponse()

