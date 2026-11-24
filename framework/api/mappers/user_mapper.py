from framework.api.models.user import UserDetails, UserPayload
from framework.models.user_registration_data import UserRegistrationData


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


def map_user_registration_data_to_user_details(user_registration_data: UserRegistrationData) -> UserDetails:
    return UserDetails(
        name=user_registration_data.name,
        email=user_registration_data.email,
        title=str(user_registration_data.salutation.value),
        birth_day=str(user_registration_data.date_of_birth.day),
        birth_month=str(user_registration_data.date_of_birth.month),
        birth_year=str(user_registration_data.date_of_birth.year),
        first_name=user_registration_data.first_name,
        last_name=user_registration_data.last_name,
        company= user_registration_data.company,
        address1=user_registration_data.address,
        address2=user_registration_data.address2,
        country=str(user_registration_data.country.value),
        zipcode=user_registration_data.zipcode,
        state=user_registration_data.state,
        city=user_registration_data.city,
    )