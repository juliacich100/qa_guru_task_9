from demo_qa.model.pages.practice_form import practice_form
from demo_qa.data.user import Sponge_Bob


def test_open_browser():
    practice_form.open_chrome()
    practice_form.fill_registration_form(Sponge_Bob)
    practice_form.submit()
    practice_form.validate_submitted_data(Sponge_Bob)