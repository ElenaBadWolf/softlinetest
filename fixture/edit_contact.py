class EditContactHelper:
    def __init__(self, app):
        self.app = app

    def edit_contact(self):
        wd = self.app.wd
        wd.get("http://93.174.133.33/")
        wd.find_element_by_css_selector(".item-field").click()
        wd.find_element_by_css_selector(".js-edit").click()
        wd.find_element_by_id("FirstName").clear()
        wd.find_element_by_id("FirstName").send_keys("EditFirstName")
        wd.find_element_by_css_selector(".js-save").click()
        contact = wd.find_element_by_css_selector(".list-data").text
        if "EditFirstName" not in contact:
            raise Exception("There is no edited contact EditFirstName")