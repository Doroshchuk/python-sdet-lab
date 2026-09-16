from dataclasses import dataclass
from datetime import date
from enum import Enum


class Salutation(Enum):
    MR = "Mr."
    MRS = "Mrs."


class Country(Enum):
    INDIA = "India"
    UNITED_STATES = "United States"
    CANADA = "Canada"
    AUSTRALIA = "Australia"
    ISRAEL = "ISRAEL"
    NEW_ZEALAND = "New Zealand"
    SINGAPORE = "Singapore"


@dataclass
class UserRegistrationData:
    # Contact Information
    email: str
    name: str
    password: str = "1111"
    salutation: Salutation = Salutation.MRS
    date_of_birth: date = date(1995, 5, 17)
    signup_for_newsletter: bool = True
    signup_for_offers: bool = True
    # Address Information
    first_name: str = "Owens"
    last_name: str = "Monica"
    company: str = "Google"
    address: str = "200 Famous Street"
    address2: str = "apt. 50"
    country: Country = Country.UNITED_STATES
    state: str = "CA"
    city: str = "San Mateo"
    zipcode: str = "94401"
    mobile_number: str = "+15137206700"
