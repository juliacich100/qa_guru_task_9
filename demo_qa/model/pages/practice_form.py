from selene.support.shared import browser
from selene import have, command, be
import config
from demo_qa.model.controls import radio, checkboxes
from demo_qa.model.controls.dropdowns import Dropdowns
from demo_qa.model.controls.datepicker import Datepicker
from demo_qa.utils import paths
from demo_qa.data.user import User




class PracticeForm:
    def __init__(self):
        self.firstName = browser.element('#firstName')
        self.lastName = browser.element('#lastName')
        self.userEmail = browser.element('#userEmail')
        self.gender = radio.Buttons('[name=gender]')
        self.phoneNumber = browser.element('#userNumber')
        self.hobbies = checkboxes.Hobbies('[for^=hobbies-checkbox]')
        self.subject = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.birthday = Datepicker(browser.element('#dateOfBirthInput'))
        self.state = Dropdowns(browser.element('#state'))
        self.city = Dropdowns(browser.element('#city'))

    def open_chrome(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        ads.should(have.size_less_than_or_equal(3))
        ads.perform(command.js.remove)
        return self

    def fill_registration_form(self, user: User):
        self.firstName.type(user.first_name)
        self.lastName.type(user.last_name)
        self.userEmail.type(user.email)
        self.gender.select_option(user.gender)
        self.phoneNumber.type(user.phone_number)
        self.hobbies.select_options(user.hobbies)
        self.subject.type(user.subject).press_enter()
        self.picture.send_keys(paths.path_to_image(user.picture))
        self.address.type(user.address)
        self.birthday.select_date_of_birth(user.birthday)
        self.state.select_option(user.state)
        self.city.select_option(user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def validate_submitted_data(self, user: User):
        browser.element('.modal-content').should(be.present)
        browser.element('.table').all('td').even.should(have.texts(
            user.first_name + ' ' + user.last_name,
            user.email,
            user.gender,
            user.phone_number,
            user.birthday.strftime(config.date_view_format),
            user.subject,
            user.hobbies,
            user.picture,
            user.address,
            user.state + ' ' + user.city))
        return self


practice_form = PracticeForm()