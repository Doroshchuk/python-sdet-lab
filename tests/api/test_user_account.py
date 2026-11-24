from dataclasses import asdict, dataclass
import pytest
from playwright.sync_api import APIRequestContext

from framework.factories.user_registration_data_factory import (
    UserRegistrationDataFactory,
)
from framework.models.user_registration_data import UserRegistrationData
from framework.api.user_payload_mapper import map_user_registration_data_to_payload


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
    user_data = map_user_registration_data_to_payload(user_registration_data)
    register_user_cleanup(user_data.email, user_data.password)

    account_created_response = api_request_context.post(
        url="/api/createAccount", form=asdict(user_data)
    )
    account_created_response_data = account_created_response.json()
    
    assert account_created_response.ok
    assert account_created_response_data["responseCode"] == 201
    assert account_created_response_data["message"] == "User created!"

    account_response = api_request_context.get(
        url="/api/getUserDetailByEmail", params={"email": user_data.email}
    )
    account_response_data = account_response.json()
    assert account_response.ok
    assert account_response_data["responseCode"] == 200
    assert account_response_data["user"]["first_name"] == user_data.firstname
    assert account_response_data["user"]["last_name"] == user_data.lastname
