import pytest
from playwright.sync_api import expect

from framework.config.settings import BASE_URL
from framework.pages.home_page import HomePage
from framework.pages.signup_login_page import SignupAndLoginPage
from framework.utils.common import (
    build_url,
    generate_random_email,
    generate_random_string,
)
from framework.utils.ui import ValidityState, get_validity_state


# Test Case 3
def test_login_with_invalid_credentials(home_page: HomePage) -> None:
    login_page = home_page.header.go_to_signup_login_page()

    expect(login_page.login_form_title).to_be_visible()
    login_page.login(generate_random_email(), generate_random_string())
    expect(login_page.login_error).to_be_visible()


# Verify that browser-native HTML email constraints work correctly
@pytest.mark.parametrize(
    "email, password, expected_validity",
    [
        pytest.param(
            "",
            ValidityState(valid=False, valueMissing=True),
            id="email_required",
        ),
        pytest.param(
            "emailexample.com",
            ValidityState(valid=False, typeMismatch=True),
            id="email_without_at_symbol",
        ),
        pytest.param(
            "@example.com",
            ValidityState(valid=False, typeMismatch=True),
            id="email_without_username",
        ),
        pytest.param(
            "email@.com",
            ValidityState(valid=False, typeMismatch=True),
            id="email_without_domain",
        ),
        pytest.param(
            "email@example.",
            ValidityState(valid=False, typeMismatch=True),
            id="email_without_top_level_domain",
        ),
        pytest.param(
            "email@.example.com",
            ValidityState(valid=False, typeMismatch=True),
            id="email_without_subdomain",
        ),
    ],
)
def test_email_validity_on_login_form(
    email: str, expected_validity: ValidityState, home_page: HomePage
) -> None:
    login_page = home_page.header.go_to_signup_login_page()

    expect(login_page.login_form_title).to_be_visible()
    login_page.login(email, "ValidPassword123!")
    actual_validity = get_validity_state(login_page.login_email_input)
    assert actual_validity == expected_validity
    expect(login_page.page).to_have_url(build_url(BASE_URL, SignupAndLoginPage.PATH))
