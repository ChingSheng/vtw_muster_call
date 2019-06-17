from selenium import webdriver

import os

class MyDriver:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--lang=zh-tw')
        current_path = os.path.abspath(__file__)
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        self.driver = webdriver.Chrome(father_path+'/chromedriver', options=chrome_options)

    def getDriver(self):
        return self.driver