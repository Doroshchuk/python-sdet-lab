import pytest
from playwright.sync_api import APIRequestContext

from framework.factories.user_registration_data_factory import (
    UserRegistrationDataFactory,
)
from framework.models.user_registration_data import UserRegistrationData


@pytest.fixture
def user_registration_data() -> UserRegistrationData:
    user_registration_data = UserRegistrationDataFactory.create()
    return user_registration_data


# API Test Case 11
def test_user_account_creation(
    user_registration_data: UserRegistrationData,
    api_request_context: APIRequestContext,
    register_user_cleanup,
):
    user_data = {
        "name": user_registration_data.name,
        "email": user_registration_data.email,
        "password": user_registration_data.password,
        "title": str(user_registration_data.salutation.value),
        "birth_date": user_registration_data.date_of_birth.day,
        "birth_month": user_registration_data.date_of_birth.month,
        "birth_year": user_registration_data.date_of_birth.year,
        "firstname": user_registration_data.first_name,
        "lastname": user_registration_data.last_name,
        "company": user_registration_data.company,
        "address1": user_registration_data.address,
        "address2": user_registration_data.address2,
        "country": str(user_registration_data.country.value),
        "zipcode": user_registration_data.zipcode,
        "state": user_registration_data.state,
        "city": user_registration_data.city,
        "mobile_number": user_registration_data.mobile_number,
    }

    account_created_response = api_request_context.post(
        url="/api/createAccount", form=user_data
    )
    register_user_cleanup(user_data["email"], user_data["password"])
    account_created_response_data = account_created_response.json()
    assert account_created_response.ok
    assert account_created_response_data["responseCode"] == 201
    assert account_created_response_data["message"] == "User created!"

    account_response = api_request_context.get(
        url="/api/getUserDetailByEmail", params={"email": user_data["email"]}
    )
    account_response_data = account_response.json()
    assert account_response.ok
    assert account_response_data["responseCode"] == 200
    assert account_response_data["user"]["first_name"] == user_data["firstname"]
    assert account_response_data["user"]["last_name"] == user_data["lastname"]
