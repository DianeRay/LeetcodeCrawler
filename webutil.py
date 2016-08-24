from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os
class Selenium(object):
    def init(self):
        drivers = ['/chromedriver_mac', '/chromedriver_linux']
        for i in drivers:
            path = os.getcwd()+i
            try:
                os.environ["webdriver.chrome.driver"] = path
                return webdriver.Chrome(path)
            except OSError:
                print err.wrong_driver(path)
    '''
    def loadUrl(self, driver, url):
        try:
            return driver.get(url)
        except WebDriverException:
            err.load_url()
    '''
    def getElementsByTagName(self, driver, tag):
        try:
            return driver.find_elements_by_tag_name(tag)
        except Exception:
            print 'No such a tag:'+tag
            return []
    def getElementByTagName(self, driver, tag):
        try:
            return driver.find_element_by_tag_name(tag)
        except WebDriverException:
            print 'No such a tag:'+tag
            return None
    def getElementsByClassName(self, driver, n):
        try:
            return driver.find_elements(By.CLASS_NAME, n)
        except WebDriverException:
            print 'No such a CLASS_NAME!'+n
            return []
    def getElementByClassName(self, driver, n):
        try:
            return driver.find_element(By.CLASS_NAME, n)
        except WebDriverException:
            print 'No such a CLASS_NAME!'+n
            return None
    def getElementById(self, driver, i):
        try:
            return driver.find_element_by_id(i)
        except WebDriverException:
            print 'No such an ID'+i
            return None
    def getElementByCss(self, driver, css):
        try:
            return driver.find_element_by_css_selector(css)
        except WebDriverException:
            print 'No such an ID'+css
            return None
    def clickElement(self, button):
        try:
            button.click()
            return True
        except WebDriverException:
            print 'Button is unclickable'
            return False;
    def savePage(self, driver):
        saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL)
        saveas.perform()
        sleep(1)
        enter = ActionChains(driver).send_keys(Keys.ENTER)
