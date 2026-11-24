from dataclasses import asdict
from playwright.sync_api import APIRequestContext, APIResponse

from framework.api.models.user import UserPayload


class UserApiClient:
    CREATE_ACCOUNT_PATH = "/api/createAccount"
    GET_ACCOUNT_PATH = "/api/getUserDetailByEmail"
    DELETE_ACCOUNT_PATH = "/api/deleteAccount"

    def __init__(self, api_request_context: APIRequestContext) -> None:
        self.api_request_context = api_request_context

    def create_account(self, user_payload: UserPayload) -> APIResponse:
        return self.api_request_context.post(
            url=self.CREATE_ACCOUNT_PATH, form=asdict(user_payload)
        )

    def get_account(self, email: str) -> APIResponse:
        return self.api_request_context.get(
            url=self.GET_ACCOUNT_PATH, params={"email": email}
        )

    def delete_account(self, email: str, password: str) -> APIResponse:
        return self.api_request_context.delete(
            url=self.DELETE_ACCOUNT_PATH, form={"email": email, "password": password}
        )
        