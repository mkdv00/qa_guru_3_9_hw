from demoqa_tests.data.user import test_user
from demoqa_tests.model.pages.demoqa_page import DemoqaForm


def test_successful_completion_of_the_form(browser_config):
    form = DemoqaForm(user=test_user)
    form.submit_form() \
        .validate_form()
