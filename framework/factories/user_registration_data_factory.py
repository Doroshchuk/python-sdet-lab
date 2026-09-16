from framework.models.user_registration_data import UserRegistrationData
from framework.utils.common import generate_email, generate_random_string


class UserRegistrationDataFactory:
    @staticmethod
    def create() -> UserRegistrationData:
        name = generate_random_string(length=5, include_digits=False)
        email = generate_email(name)
        return UserRegistrationData(name=name, email=email)
