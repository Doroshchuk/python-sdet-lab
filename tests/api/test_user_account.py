from collections.abc import Callable

import pytest

from framework.api.clients.user_client import UserApiClient
from framework.api.mappers.user_mapper import (
    map_user_registration_data_to_payload,
    map_user_registration_data_to_user_details,
)
from framework.api.models.responses import (
    MessageResponse,
    UserAccountResponse,
    UserDetails,
)
from framework.models.user_registration_data import UserRegistrationData


@pytest.mark.smoke
def test_user_account_creation(
    user_registration_data: UserRegistrationData,
    user_api_client: UserApiClient,
    register_user_cleanup: Callable[[str, str], None],
):
    user_payload = map_user_registration_data_to_payload(user_registration_data)
    expected_user = map_user_registration_data_to_user_details(user_registration_data)
    register_user_cleanup(user_payload.email, user_payload.password)

    create_response = user_api_client.create_account(user_payload)
    assert create_response.ok, create_response.text()
    create_result = MessageResponse.model_validate(create_response.json())

    assert create_result.response_code == 201
    assert create_result.message == "User created!"

    get_response = user_api_client.get_account(user_payload.email)
    assert get_response.ok, get_response.text()
    get_result = UserAccountResponse.model_validate(get_response.json())

    assert get_result.response_code == 200
    actual_user = UserDetails.model_validate(get_result.user.model_dump())
    assert actual_user == expected_user
