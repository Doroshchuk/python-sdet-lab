import random
import string
from datetime import datetime


def generate_random_email(length: int = 10, domain: str = "example.com") -> str:
    """
    Generate a random email address for testing purposes.

    Args:
        length: Length of the email local part. Must be positive.
        domain: Email domain without the '@' symbol.

    Returns:
        A randomly generated email address.
    """

    username = generate_random_string(length, include_digits=True)
    return f"{username}@{domain}"


def generate_random_string(length: int = 10, include_digits: bool = False) -> str:
    """
    Generate a random string for testing purposes.

    Args:
        length: Length of the string. Must be positive.
        include_digits: Whether digits should be included in the generated string.

    Returns:
        A randomly generated string.
    """

    population = string.ascii_lowercase + (string.digits if include_digits else "")
    return "".join(random.choices(population, k=length))


def current_timestamp() -> str:
    """
    Return the current timestamp formatted for filenames.

    Returns:
        Current timestamp in YYYYMMDD_HHMMSS format.
    """

    return datetime.now().strftime("%Y%m%d_%H%M%S")


def build_url(base_url: str, path: str) -> str:
    """
    Build a URL from a base URL and path.

    Args:
        base_url: Base URL.
        path: Path to append to a base URL.

    Returns:
        A normalized URL.
    """

    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"
