from lettuce import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


@step(u'I am in the twitter front page')
def open_twitter_web(step):
    world.driver = webdriver.Firefox()
    world.driver.get("https://twitter.com/")


@step(u'I log in with the user ([^\s]+) and the password ([^\s]+)')
def login_user_password(step, username, password):
    elemIniciar = world.driver.find_element_by_css_selector('.StreamsHero-buttonContainer .Button.StreamsLogin')
    elemIniciar.click()
    elementIniciar = world.driver.find_element_by_name("session[username_or_email]")
    elementIniciar.send_keys(username)
    world.driver.implicitly_wait(1)
    world.elementContrase = world.driver.find_element_by_name("session[password]")
    world.elementContrase.send_keys(password)


@step(u'When I click the login button I log into twitter')
def log_into_twitter(step):
    world.driver.implicitly_wait(2)
    world.elementContrase.send_keys(Keys.ENTER)


@step(u'I write the tweet ([^\s]+)')
def write_tweet(step, tweet):
    world.driver.implicitly_wait(2)
    elem = world.driver.find_element_by_id("tweet-box-home-timeline")
    elem.send_keys(tweet)


@step(u'I click on the Post button a tweet is created')
def click_on_post(step):
    world.driver.find_element_by_css_selector('button.btn.primary-btn.tweet-action.tweet-btn.js-tweet-btn').click()
    world.driver.implicitly_wait(2)
    world.driver.close()

