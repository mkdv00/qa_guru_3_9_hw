from selene import have
from selene.support.shared import browser


class Checkbox:
    
    def __init__(self, selector):
        self.selector = selector

    def select_checkbox(self, value):
        browser.all(self.selector).element_by(have.text(value)).click()
