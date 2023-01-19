from selene import have
from selene.support.shared import browser


class DropDown:
    
    def __init__(self, selector):
        self.selector = selector


    def select(self, item_text):
        browser.element(self.selector).click()
        browser.all('[id^=react-select][id*=option').element_by(
            have.exact_text(item_text)
        ).click()
