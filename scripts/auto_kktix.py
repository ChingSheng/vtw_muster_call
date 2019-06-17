# -*- coding: UTF-8 -*-
import time

from selenium.webdriver.common.keys import Keys

from chromedriver.MyDriver import MyDriver
from content import kktix_event_content
from setting import account
from utils.FutureDay import FutureDay

class VTW_KKTIX_Script:
    SHORT_DELAY = 1
    NORMAL_DELAY = 2
    LONG_DELAY = 5
    SUPER_LONG_DELAY = 10

    def __init__(self, hackMdUrl="Unknown"):
        myDriver = MyDriver()
        self.hackMdUrl = hackMdUrl
        self.driver = myDriver.getDriver()

    def go(self):
        self.driver.get('https://kktix.com/users/sign_in')
        time.sleep(self.NORMAL_DELAY)

    def loginKKTIX(self):
        self.driver.find_element_by_id("user_login").send_keys(account.kktix_account)
        self.driver.find_element_by_id("user_password").send_keys(account.kktix_password)
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_name("commit").click()
        time.sleep(self.SHORT_DELAY)

    def goOpenActivity(self):
        self.driver.get('https://kktix.com/dashboard/events/new?organization=vtaiwan')
        time.sleep(self.SHORT_DELAY)

    def chooseEmptyTemplate(self):
        elements = self.driver.find_elements_by_class_name("radio")
        elements[0].click()
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def setTitle(self):
        self.driver.find_element_by_id("event_name").send_keys(kktix_event_content.title.decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def storeUrl(self):
        self.url = "https://vtaiwan.kktix.cc/events/" + self.driver.find_element_by_name("event[slug]").get_attribute("value")
        print self.url

    def setTime(self):
        futureDay = FutureDay()
        daysAhead = futureDay.days_ahead(2) # 2 = Wed
        next_wednesday = futureDay.next_weekend(2).strftime("%Y/%m/%d")
        print daysAhead
        print next_wednesday
        dateElements = self.driver.find_elements_by_class_name("datepicker")
        timeElements = self.driver.find_elements_by_class_name("ui-timepicker-input")

        dateElements[0].click()
        time.sleep(self.SHORT_DELAY)

        # 保險起見，先點擊當天的日期，再按下右鍵
        self.driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-days > table > tfoot > tr:nth-child(1) > th").click()
        dateElements[0].click()

        time.sleep(self.SHORT_DELAY)
        for i in range(daysAhead):
            dateElements[0].send_keys(Keys.RIGHT)

        dateElements[0].send_keys(Keys.ENTER)
        dateElements[0].send_keys(Keys.TAB)
        timeElements[0].send_keys(Keys.BACK_SPACE)
        timeElements[0].send_keys("19:00")
        timeElements[0].send_keys(Keys.ENTER)
        time.sleep(self.SHORT_DELAY)

        timeElements[0].send_keys(Keys.TAB)
        dateElements[1].send_keys(next_wednesday)
        dateElements[1].send_keys(Keys.TAB)
        timeElements[1].send_keys(Keys.BACK_SPACE)
        timeElements[1].send_keys("21:00")
        timeElements[1].send_keys(Keys.ENTER)
        time.sleep(self.SHORT_DELAY)

    def setMetaData(self):
        self.driver.find_element_by_id("event_capacity").clear()
        self.driver.find_element_by_id("event_capacity").send_keys("15")
        self.driver.find_element_by_id("event_location").send_keys("社會創新實驗中心(2樓A9會議室)".decode('utf8'))
        self.driver.find_element_by_id("event_location_address").send_keys("台北市大安區仁愛路三段99號".decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def setDescription(self):
        self.driver.find_element_by_class_name("cke_button__source").click()
        time.sleep(self.SHORT_DELAY)
        body_string =kktix_event_content.description.format(self.hackMdUrl, self.hackMdUrl)
        self.driver.find_element_by_class_name("cke_contents_ltr").send_keys((body_string).decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def goTicketSetting(self):
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def goFormSetting(self):
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def disableCheckBoxPhone(self):
        self.driver.find_element_by_css_selector("#new-event > div > div:nth-child(4) > div > div.contact-block.ng-scope > div > div.col-4 > table > tbody > tr:nth-child(3) > td > label > input").click()
        time.sleep(self.LONG_DELAY)

    def clickConfirm(self):
        self.driver.find_element_by_class_name("btn btn-primary").click()

    def run(self, debugMode = False):
        try:
            self.go()
            self.loginKKTIX()
            self.goOpenActivity()
            self.chooseEmptyTemplate()
            self.setTitle()
            self.storeUrl()
            self.setTime()
            self.setMetaData()
            self.setDescription()
            self.goTicketSetting()
            self.goFormSetting()
            self.disableCheckBoxPhone()
            if not debugMode:
                self.clickConfirm()

        except Exception as e:
            print e
        finally:
            self.driver.close()
            return self.url

if __name__ == "__main__":
    script = VTW_KKTIX_Script(True)
    script.run()

