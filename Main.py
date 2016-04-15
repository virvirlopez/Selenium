from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# vickiviki2

driver = webdriver.Firefox()
driver.get("https://twitter.com/")
driver.implicitly_wait(10)
elemIniciar = driver.find_element_by_css_selector('.StreamsHero-buttonContainer .Button.StreamsLogin')
elemIniciar.click()
elementIniciar = driver.find_element_by_name("session[username_or_email]")
elementIniciar.send_keys("vickiviki2")
driver.implicitly_wait(1)
elementContrase = driver.find_element_by_name("session[password]")
elementContrase.send_keys("maylopez")
driver.implicitly_wait(2)
elementContrase.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
elem = driver.find_element_by_id("tweet-box-home-timeline")
elem.send_keys("I am using Selenium!! viva")
driver.find_element_by_css_selector('button.btn.primary-btn.tweet-action.tweet-btn.js-tweet-btn').click()
driver.implicitly_wait(10)
driver.close()
