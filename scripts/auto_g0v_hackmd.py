# -*- coding: UTF-8 -*-
import time
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
        self.driver.find_element_by_id("create-note-menu").click()
        time.sleep(self.LONG_DELAY)
        elements = self.driver.find_elements_by_class_name("menu-item")
        for element in elements:
            if unicode(element.text) == u"vTaiwan小松":
                element.click()
        time.sleep(self.NORMAL_DELAY)

    # Need help!
    def modify_template(self):
        pass

    def delete_current_note(self):
        self.driver.find_element_by_class_name("fa-unlock-alt").click()
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
