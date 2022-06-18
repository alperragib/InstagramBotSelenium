from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import requests 

class Instagram:

    def __init__(self,email,password):
        self.browser = webdriver.Chrome("C:/Users/alper/PythonProjects/InstagramBotProject/chromedriver.exe")
        self.email = email
        self.password = password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        emailInput = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input""")
        passInput = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input""")
        emailInput.send_keys(self.email)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def getFollowers(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(5)
        followersLink = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""")
        followersLink.click()
        time.sleep(7)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"ilk sayım: {followerCount}")
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if newCount<200:
                followerCount = newCount
                print(f"yeni sayım: {newCount}")
                time.sleep(2)
            else:
                break

        
        i=0
        while i<2:
            dialog.click()
            action.key_down(Keys.SPACE).perform()
            time.sleep(1)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            print(f"yeni sayım: {newCount}")
            i=i+1

        followers = dialog.find_elements_by_css_selector("li")
        
        for user in followers:
            fol_button = user.find_element_by_css_selector("button")
            if fol_button.text == "Takip Et":
                fol_button.click()
                print("Takip Edildi :)")
                time.sleep(3)

        self.browser.quit()

instagram = Instagram("username","password")
instagram.signIn()
instagram.getFollowers("username")


