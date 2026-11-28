from dataclasses import dataclass


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
