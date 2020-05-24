#Imports some stuff from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
#pyautogui allows me to click on the windows file prompt when it appears
import pyautogui
import time
import sys

#Username and password
username = "username"
passwd = "password"
#Location of the chrome driver that allows selenium to work with it
driverpth = "chromedriver.exe"


options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#The location of the chrome binary
options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
#The user agent the browser is pretending to be
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://www.instagram.com/accounts/login/")
#The driver will wait up to 10 seconds for an element to appear on screen
driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
time.sleep(4)
driver.get("https://www.instagram.com/")
driver.find_element_by_xpath("//div[@class='mt3GC']/button[1]").click()
driver.find_element_by_xpath("//div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
#Wait 5 seconds for the file dialog box to appear
#Unfortuanetly, I couldn't find a way to get pyautogui to just detect when the file explorer prompt appears
#so I wait 5 seconds as a precaution
time.sleep(5)
pyautogui.write(sys.argv[1], interval=0.05)
pyautogui.press('enter')
driver.find_element_by_xpath("//div[1]/section/div[1]/header/div/div[2]/button").click()
driver.find_element_by_xpath("//div[1]/section/div[2]/section[1]/div/textarea").send_keys(sys.argv[2])
driver.find_element_by_xpath("//div[1]/section/div[1]/header/div/div[2]/button").click()
driver.close()

