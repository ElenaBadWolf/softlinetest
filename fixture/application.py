from selenium import webdriver
from fixture.add_new_contact import NewContactHelper
from fixture.edit_contact import EditContactHelper
from fixture.delete_contact import DeleteContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
           self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver. Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.add_new_contact = NewContactHelper(self)
        self.edit_contact = EditContactHelper(self)
        self.delete_contact = DeleteContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()