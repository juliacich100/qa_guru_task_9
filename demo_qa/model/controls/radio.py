from selene.support.shared import browser
from selene import have


class Buttons:
    def __init__(self, buttons):
        self.buttons = buttons

    def select_option(self, gender):
        browser.all(self.buttons).element_by(have.value(gender)).element('..').click()