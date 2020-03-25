# -*- coding: UTF-8 -*-
import time
import sys
sys.path.append('../')

from chromedriver.my_driver import MyDriver
from setting import account

class G0vHackMdScript:
    SHORT_DELAY = 1
    NORMAL_DELAY = 2
    LONG_DELAY = 5
    SUPER_LONG_DELAY = 10

    def __init__(self):
        myDriver = MyDriver()
        self.driver = myDriver.getDriver()

    def browse(self):
        self.driver.get('https://g0v.hackmd.io/login')
        time.sleep(self.NORMAL_DELAY)

    def direct_login(self):
        self.driver.find_element_by_name("email").send_keys(account.hackmd_account)
        self.driver.find_element_by_name("password").send_keys(account.hackmd_password)
        self.driver.find_element_by_css_selector("input[formaction='https://g0v.hackmd.io/login']").click()
        time.sleep(self.LONG_DELAY)

    def create_note_and_choose_template(self):
        self.driver.find_element_by_class_name("sidenav-item-action").click()
        time.sleep(self.LONG_DELAY)
        self.driver.find_element_by_css_selector("#sidebar > div.ui-next-sidenav-inner > div.ui-next-sidenav-create.sidenav-item > div > div.menu-container.base-menu.position-bottom > div:nth-child(2)").click()
        time.sleep(self.NORMAL_DELAY)
        elements = self.driver.find_elements_by_class_name("list-group-item-heading")
        for element in elements:
            if unicode(element.text) == u"vTaiwan小松":
                element.click()
        time.sleep(self.SHORT_DELAY)
        self.driver.find_element_by_css_selector("#templateModal > div > div > div.modal-body > div > div.col-sm-4.template-list-container > div > button.btn.btn-primary.ui-use-template-btn.hidden-xs").click()
        time.sleep(self.LONG_DELAY)

    # Need help!
    def modify_template(self):
        pass
        # self.driver.find_element_by_class_name("fa-pencil").click()
        # time.sleep(self.NORMAL_DELAY)
        # element = self.driver.find_element_by_class_name("CodeMirror-line")
        # element.click()
        # time.sleep(self.NORMAL_DELAY)

    def delete_current_note(self):
        self.driver.find_element_by_class_name("ui-menu").click()
        time.sleep(self.NORMAL_DELAY)
        self.driver.find_element_by_class_name("ui-delete-note").click()
        time.sleep(self.NORMAL_DELAY)
        self.driver.find_element_by_class_name("ui-delete-modal-confirm").click()
        time.sleep(self.SHORT_DELAY)

    def run(self, debug_mode=False):
        try :
            self.browse()
            self.direct_login()
            self.create_note_and_choose_template()
            self.url = self.driver.current_url
            self.modify_template()
            if debug_mode:
                self.delete_current_note()
        except Exception as e:
            print e
        finally:
            self.driver.close()
            return self.url

if __name__ == "__main__":
    script = G0vHackMdScript()
    result = script.run(True)
    print result
