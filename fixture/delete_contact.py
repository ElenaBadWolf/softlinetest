class DeleteContactHelper:
    def __init__(self, app):
        self.app = app

    def delete_contact(self):
        wd = self.app.wd
        wd.get("http://93.174.133.33/")
        wd.find_element_by_css_selector(".item-field").click()
        wd.find_element_by_css_selector(".js-delete").click()
        contact = wd.find_element_by_css_selector(".list-data").text
        if "FirstName" in contact:
            raise Exception("The conact was not deleted")