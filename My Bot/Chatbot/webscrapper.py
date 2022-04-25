from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
except:
    pass

def getresponse():
    text = open('../STT/speachoutput.txt','r')
    send_text_main(text.read())
    print("Finished Task")


def send_text_main(text):
        textboxmain = driver.find_element_by_id("avatarform")
        textbox = textboxmain.find_element_by_class_name("stimulus")

        textbox.send_keys(text)
        textbox.send_keys(Keys.RETURN)
        time.sleep(5)

        line1 = driver.find_element_by_id("line1")
        fd = open("response_stream", "w")
        fd.write(line1.text)
        fd.close()

if __name__ == "__main__":
    getresponse()

