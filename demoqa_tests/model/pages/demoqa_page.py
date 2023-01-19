from selene import have, command
from selene.support.shared import browser

from demoqa_tests.data.user import User
from demoqa_tests.model.contrlos.checkboxes import Checkbox
from demoqa_tests.model.contrlos.dropdown import DropDown
from demoqa_tests.model.contrlos.options_select import Select
from demoqa_tests.model.contrlos.radio_button import RadioButton
from demoqa_tests.utils import resources


class DemoqaForm:

    def __init__(self, user: User):
        self.user = user
        self.state = browser.element('#state')

    def open_demo_qa_automation_practice_form(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)

    def set_name(self):
        browser.element('#firstName').type(self.user.first_name)

    def set_last_name(self):
        browser.element('#lastName').type(self.user.last_name)

    def set_email(self):
        browser.element('#userEmail').type(self.user.email)

    def select_gender(self):
        RadioButton('[name=gender]').select_radio(self.user.gender)

    def set_mobile_number(self):
        browser.element('#userNumber').type(self.user.phone_number)

    def select_month(self):
        browser.element('.react-datepicker__month-select').click()
        Select.select_by_text('.react-datepicker__month-select', self.user.month)

    def select_year(self):
        browser.element('.react-datepicker__year-select').click()
        Select.select_by_text('.react-datepicker__year-select', self.user.year)

    def add_birthday(self):
        browser.element('#dateOfBirthInput').click()
        self.select_month()
        self.select_year()
        self.select_day()

    def select_day(self):
        browser.element(f'.react-datepicker__day--0{self.user.day}').click()

    def set_subject(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

    def set_hobbies(self):
        Checkbox('[for^="hobbies-checkbox"]').select_checkbox(self.user.hobby)

    def upload_file(self):
        resources.select_file('#uploadPicture', self.user.picture)

    def set_current_address(self):
        browser.element('#currentAddress').type(self.user.address)

    def set_state(self):
        DropDown('#state').select(self.user.state)

    def set_city(self):
        DropDown('#city').select(self.user.city)

    def submit(self):
        browser.element('#submit').press_enter()

    def scroll_to_bottom(self):
        self.state.perform(command.js.scroll_into_view)

    def validation(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def submit_form(self):
        self.open_demo_qa_automation_practice_form()
        self.set_name()
        self.set_last_name()
        self.set_email()
        self.select_gender()
        self.set_mobile_number()
        self.add_birthday()
        self.set_subject()
        self.set_hobbies()
        self.upload_file()
        self.set_current_address()
        self.set_state()
        self.set_city()
        self.submit()
        return self

    def validate_form(self):
        user_birth = f'{self.user.day} {self.user.month},{self.user.year}'
        user_full_name = self.user.first_name + ' ' + self.user.last_name
        user_place = self.user.state + ' ' + self.user.city
        user_picture = self.user.picture.split('/')[1]

        self.validation(
            user_full_name,
            self.user.email,
            self.user.gender,
            self.user.phone_number,
            user_birth,
            self.user.subject,
            self.user.hobby,
            user_picture,
            self.user.address,
            user_place
        )
