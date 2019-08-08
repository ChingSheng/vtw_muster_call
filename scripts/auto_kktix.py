# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')

import time
from selenium.webdriver.common.keys import Keys
from chromedriver.my_driver import MyDriver
from content import kktix_event_content
from setting import account
from utils.future_day import FutureDay


class VtwKKTixScript:
    SHORT_DELAY = 1
    NORMAL_DELAY = 2
    LONG_DELAY = 5
    SUPER_LONG_DELAY = 10

    def __init__(self, hackMdUrl="Unknown"):
        myDriver = MyDriver()
        self.hackMdUrl = hackMdUrl
        self.driver = myDriver.getDriver()
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)

    def browse(self):
        self.driver.get('https://kktix.com/users/sign_in')
        time.sleep(self.NORMAL_DELAY)

    def login_kktix(self):
        self.driver.find_element_by_id("user_login").send_keys(account.kktix_account)
        self.driver.find_element_by_id("user_password").send_keys(account.kktix_password)
        time.sleep(self.SHORT_DELAY)
        try:
            self.driver.find_element_by_name("commit").click()
        except:
            print 'go vtaiwan page timeout?'
            self.driver.execute_script('window.stop()')
        time.sleep(self.SHORT_DELAY)

    def browse_open_activity(self):
        self.driver.get('https://kktix.com/dashboard/events/new?organization=vtaiwan')
        time.sleep(self.SHORT_DELAY)

    def choose_empty_template(self):
        elements = self.driver.find_elements_by_class_name("radio")
        elements[0].click()
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def set_title(self):
        self.driver.find_element_by_id("event_name").send_keys(kktix_event_content.title.decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def store_url(self):
        self.url = "https://vtaiwan.kktix.cc/events/" + self.driver.find_element_by_name("event[slug]").get_attribute(
            "value")

    def set_time(self):
        future_day = FutureDay()
        days_Ahead = future_day.days_ahead(2)  # 2 = Wed
        next_wednesday = future_day.next_weekend(2).strftime("%Y/%m/%d")
        print days_Ahead
        print next_wednesday
        date_elements = self.driver.find_elements_by_class_name("datepicker")
        time_elements = self.driver.find_elements_by_class_name("ui-timepicker-input")

        date_elements[0].click()
        time.sleep(self.SHORT_DELAY)

        # 保險起見，先點擊當天的日期，再按下右鍵(是說當日的23:40～24:00）會fail
        self.driver.find_element_by_css_selector(
            "body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-days > table > tfoot > tr:nth-child(1) > th").click()
        date_elements[0].click()

        time.sleep(self.SHORT_DELAY)
        for i in range(days_Ahead):
            date_elements[0].send_keys(Keys.RIGHT)

        date_elements[0].send_keys(Keys.ENTER)
        date_elements[0].send_keys(Keys.TAB)
        time_elements[0].send_keys(Keys.BACK_SPACE)
        time_elements[0].send_keys("19:00")
        time_elements[0].send_keys(Keys.ENTER)
        time.sleep(self.SHORT_DELAY)

        time_elements[0].send_keys(Keys.TAB)
        date_elements[1].send_keys(next_wednesday)
        date_elements[1].send_keys(Keys.TAB)
        time_elements[1].send_keys(Keys.BACK_SPACE)
        time_elements[1].send_keys("21:00")
        time_elements[1].send_keys(Keys.ENTER)
        time.sleep(self.SHORT_DELAY)

    def set_meta_data(self):
        self.driver.find_element_by_id("event_capacity").clear()
        self.driver.find_element_by_id("event_capacity").send_keys(kktix_event_content.ticket_limit)
        self.driver.find_element_by_id("event_location").send_keys("社會創新實驗中心(2樓A9會議室)".decode('utf8'))
        self.driver.find_element_by_id("event_location_address").send_keys("台北市大安區仁愛路三段99號".decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def set_description(self):
        self.driver.find_element_by_class_name("cke_button__source").click()
        time.sleep(self.SHORT_DELAY)
        body_string = kktix_event_content.description.format(self.hackMdUrl, self.hackMdUrl)
        self.driver.find_element_by_class_name("cke_contents_ltr").send_keys((body_string).decode('utf8'))
        time.sleep(self.SHORT_DELAY)

    def go_ticket_setting(self):
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def set_ticket(self):
        self.driver.find_element_by_css_selector(
            "#new-event > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > button").click()
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_css_selector(
            "#new-event > div > div:nth-child(3) > div > table > tbody > tr.edit.highlight > td > div.clearfix > div.control-group.col-3.col-last > div > label > input").click()
        time.sleep(self.SHORT_DELAY)
        element = self.driver.find_element_by_css_selector(
            "#new-event > div > div:nth-child(3) > div > table > tbody > tr.edit.highlight > td > div.clearfix > div.control-group.col-2 > div > div > input")
        element.clear()
        element.send_keys(kktix_event_content.ticket_limit)
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_css_selector(
            "#new-event > div > div:nth-child(3) > div > table > tbody > tr.edit.highlight > td > div.form-actions.plain.ng-scope > button.btn.btn-minor").click()
        time.sleep(self.SHORT_DELAY)

    def go_form_setting(self):
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.SHORT_DELAY)

    def disable_check_box_phone(self):
        self.driver.find_element_by_css_selector(
            "#new-event > div > div:nth-child(4) > div > div.contact-block.ng-scope > div > div.col-4 > table > tbody > tr:nth-child(3) > td > label > input").click()
        time.sleep(self.NORMAL_DELAY)

    def click_confirm(self):
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(self.LONG_DELAY)

    def publish(self):
        time.sleep(self.NORMAL_DELAY)
        self.driver.find_element_by_css_selector(
            "body > div.page > div.sidebar > div.point-block.unpublished > div > a").click()
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_css_selector(
            "body > div.page > div.sidebar > div.point-block.unpublished > div > ul > li > a").click()
        time.sleep(self.LONG_DELAY)

    def run(self, debug_mode=False):
        try:
            self.browse()
            self.login_kktix()
            self.browse_open_activity()
            self.choose_empty_template()
            self.set_title()
            self.store_url()
            self.set_time()
            self.set_meta_data()
            self.set_description()
            self.go_ticket_setting()
            self.set_ticket()
            self.go_form_setting()
            self.disable_check_box_phone()
            if not debug_mode:
                self.click_confirm()
                self.publish()

        except Exception as e:
            print e
        finally:
            self.driver.close()
            return self.url


if __name__ == "__main__":
    script = VtwKKTixScript()
    script.run(True)
