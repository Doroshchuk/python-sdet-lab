import pytest
from playwright.sync_api import expect

from framework.config.settings import BASE_URL
from framework.pages.signup_and_login_page import SignupAndLoginPage
from framework.utils.common import (
    build_url,
    generate_random_email,
    generate_random_string,
)
from framework.utils.ui import ValidityState, get_validity_state


# Test Case 3
def test_login_with_invalid_credentials(signup_login_page: SignupAndLoginPage) -> None:
    expect(signup_login_page.login_form_title).to_be_visible()
    signup_login_page.login(generate_random_email(), generate_random_string())
    expect(signup_login_page.login_error).to_be_visible()


# Verify that browser-native HTML email constraints work correctly
@pytest.mark.parametrize(
    "email, expected_validity",
    [
        pytest.param(
            "",
            ValidityState(valid=False, value_missing=True),
            id="email_required",
        ),
        pytest.param(
            "emailexample.com",
            ValidityState(valid=False, type_mismatch=True),
            id="email_without_at_symbol",
        ),
        pytest.param(
            "@example.com",
            ValidityState(valid=False, type_mismatch=True),
            id="email_without_username",
        ),
        pytest.param(
            "email@.com",
            ValidityState(valid=False, type_mismatch=True),
            id="email_without_domain",
        ),
        pytest.param(
            "email@example.",
            ValidityState(valid=False, type_mismatch=True),
            id="email_without_top_level_domain",
        ),
        pytest.param(
            "email@.example.com",
            ValidityState(valid=False, type_mismatch=True),
            id="email_without_subdomain",
        ),
    ],
)
def test_email_validity_on_login_form(
    email: str, expected_validity: ValidityState, signup_login_page: SignupAndLoginPage
) -> None:
    signup_login_page.login(email, "ValidPassword123!")
    actual_validity = get_validity_state(signup_login_page.login_email_input)
    assert actual_validity == expected_validity
    expect(signup_login_page.page).to_have_url(
        build_url(BASE_URL, SignupAndLoginPage.PATH)
    )
