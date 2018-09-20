class NewContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self):
        wd = self.app.wd
        wd.get("http://93.174.133.33/")
        wd.find_element_by_css_selector(".js-create").click()
        wd.find_element_by_id("FirstName").send_keys("FirstName")
        wd.find_element_by_id("SecondName").send_keys("SecondName")
        wd.find_element_by_id("SureName").send_keys("SureName")
        wd.find_element_by_id("PhoneStringValue").send_keys("7(111)3357711")
        wd.find_element_by_id("Email").send_keys("test@test.test")
        wd.find_element_by_css_selector(".js-save").click()
        contact = wd.find_element_by_css_selector(".list-data").text
        if "FirstName" not in contact:
            raise Exception("There is no new Contact FirstName")
