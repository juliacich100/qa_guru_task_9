from selene.support.shared import browser
from selene import have


class Hobbies:
    def __init__(self, element):
        self.element = element

    def select_options(self, value):
        browser.all(self.element).element_by(have.text(value)).click()