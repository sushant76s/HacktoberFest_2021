#install selenium
# add in your username, password
# add a video or playlist and run script

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

username = "YOUR USERNAME"
password = "YOUR PASSWORD"

def youtube_login():
    driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    elem = driver.find_element_by_id("identifierId")
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element_by_name("password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

def playlist():
    driver.get("LINK TO YOUR PLAYLIST")
    time.sleep(5)

def  skip_ad():
    skipbutton = driver.find_element_by_id("ad-text:t")
    skipbutton.click()

youtube_login()
playlist()
skip_ad()