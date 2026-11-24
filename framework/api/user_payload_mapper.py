from dataclasses import dataclass
from framework.models.user_registration_data import UserRegistrationData

@dataclass
class UserPayload:
    name: str
    email: str
    password: str
    title: str
    birth_date: int
    birth_month: int
    birth_year: int
    firstname: str
    lastname: str
    company: str
    address1: str
    address2: str
    country: str
    zipcode: str
    state: str
    city: str
    mobile_number: str

def map_user_registration_data_to_payload(user_registration_data: UserRegistrationData) -> UserPayload:
    return UserPayload(
        name=user_registration_data.name,
        email=user_registration_data.email,
        password=user_registration_data.password,
        title=str(user_registration_data.salutation.value),
        birth_date=user_registration_data.date_of_birth.day,
        birth_month=user_registration_data.date_of_birth.month,
        birth_year=user_registration_data.date_of_birth.year,
        firstname=user_registration_data.first_name,
        lastname=user_registration_data.last_name,
        company= user_registration_data.company,
        address1=user_registration_data.address,
        address2=user_registration_data.address2,
        country=str(user_registration_data.country.value),
        zipcode=user_registration_data.zipcode,
        state=user_registration_data.state,
        city=user_registration_data.city,
        mobile_number=user_registration_data.mobile_number,
    )