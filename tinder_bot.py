from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import numpy as np
from numpy import random

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None
            return element

        self.driver.get('https://tinder.com')

        sleep(4)

        check_more_options = check_exists_by_xpath('//button[text()="More Options"]')
        if (check_more_options != None):
            check_more_options.click()
        
        accept_cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/div/button')
        accept_cookie.click()
        
        sleep(2)

        fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(4)

        popup_1 = self.driver.find_element_by_css_selector('button[aria-label="Allow"]')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_css_selector('button[aria-label="Not interested"]')
        popup_2.click()
        
        sleep(4)

        passport_popup = self.driver.find_element_by_css_selector('button[aria-label="Close"]')
        passport_popup.click()
        
        #self.auto_swipe()
        self.alt_swipe()
        
    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Like"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Nope"]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_tinder_plus()

    def alt_swipe(self):
        while True:
            sleep(2)
            try:
                coin = np.random.binomial(n=1, p=0.5, size=None)
                if coin == 1:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_tinder_plus()
    
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//span[text()="Not interested"]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//a[text()="Keep Swiping"]')
        match_popup.click()

    def close_tinder_plus(self):
        tinder_plus_popup =  self.driver.find_element_by_xpath('//span[text()="No Thanks"]')
        tinder_plus_popup.click()
        self.driver.quit()
        exit(0)

bot = TinderBot()
bot.login()
