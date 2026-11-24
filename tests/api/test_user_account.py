from dataclasses import asdict
import pytest
from playwright.sync_api import APIRequestContext

from framework.api.models.user import UserDetails, UserResponse
from framework.factories.user_registration_data_factory import (
    UserRegistrationDataFactory,
)
from framework.models.user_registration_data import UserRegistrationData
from framework.api.mappers.user_mapper import map_user_registration_data_to_payload, map_user_registration_data_to_user_details


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
    user_payload = map_user_registration_data_to_payload(user_registration_data)
    expected_user = map_user_registration_data_to_user_details(user_registration_data)
    register_user_cleanup(user_payload.email, user_payload.password)

    account_created_response = api_request_context.post(
        url="/api/createAccount", form=asdict(user_payload)
    )
    account_created_response_data = account_created_response.json()

    assert account_created_response.ok
    assert account_created_response_data["responseCode"] == 201
    assert account_created_response_data["message"] == "User created!"

    account_response = api_request_context.get(
        url="/api/getUserDetailByEmail", params={"email": user_payload.email}
    )
    assert account_response.ok
    account_response_data = account_response.json()
    assert account_response_data["responseCode"] == 200
    actual_user = UserResponse(**account_response_data["user"])
    assert type(actual_user.id) is int
    assert UserDetails.from_user_response(actual_user) == expected_user
    
