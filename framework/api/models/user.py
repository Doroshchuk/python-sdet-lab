from dataclasses import dataclass, fields

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


@dataclass
class UserDetails:
    name: str
    email: str
    title: str
    birth_day: str
    birth_month: str
    birth_year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str

    @classmethod
    def from_user_response(cls, user_response: "UserResponse") -> "UserDetails":
        return cls(
            **{
                field.name: getattr(user_response, field.name)
                for field in fields(cls)
            }
        )


@dataclass
class UserResponse(UserDetails):
    id: int