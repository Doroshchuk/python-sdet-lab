import calendar
from datetime import date

from playwright.sync_api import Page

from framework.models.user_registration_data import Salutation, UserRegistrationData
from framework.pages.account_created_page import AccountCreatedPage
from framework.pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Account Information
        self.account_info_title = self.page.get_by_role(
            "heading", name="Enter Account Information"
        )
        self.mr_radio_button = self.page.get_by_role("radio", name="Mr.")
        self.mrs_radio_button = self.page.get_by_role("radio", name="Mrs.")
        self.name_input = self.page.get_by_test_id("name")
        self.email_input = self.page.get_by_test_id("email")
        self.password_input = self.page.get_by_test_id("password")
        self.dob_day_selector = self.page.get_by_test_id("days")
        self.dob_month_selector = self.page.get_by_test_id("months")
        self.dob_year_selector = self.page.get_by_test_id("years")
        self.newsletter_checkbox = self.page.get_by_role(
            "checkbox", name="Sign up for our newsletter!"
        )
        self.offers_checkbox = self.page.get_by_role(
            "checkbox", name="Receive special offers from our partners!"
        )

        # Address Information
        self.first_name_input = self.page.get_by_test_id("first_name")
        self.last_name_input = self.page.get_by_test_id("last_name")
        self.company_input = self.page.get_by_test_id("company")
        self.address_input = self.page.get_by_test_id("address")
        self.address2_input = self.page.get_by_test_id("address2")
        self.country_selector = self.page.get_by_test_id("country")
        self.state_input = self.page.get_by_test_id("state")
        self.city_input = self.page.get_by_test_id("city")
        self.zipcode_input = self.page.get_by_test_id("zipcode")
        self.mobile_number_input = self.page.get_by_test_id("mobile_number")

        self.create_account_button = self.page.get_by_role(
            "button", name="Create Account"
        )

    def select_salutation(self, salutation: Salutation) -> None:
        if salutation == Salutation.MR:
            self.mr_radio_button.check()
        elif salutation == Salutation.MRS:
            self.mrs_radio_button.check()

    def set_date_of_birth(self, dob: date) -> None:
        self.dob_day_selector.select_option(str(dob.day))
        self.dob_month_selector.select_option(calendar.month_name[dob.month])
        self.dob_year_selector.select_option(str(dob.year))

    def create_account(self, user_data: UserRegistrationData) -> AccountCreatedPage:
        # Account Information
        self.select_salutation(user_data.salutation)
        self.password_input.fill(user_data.password)
        self.set_date_of_birth(user_data.date_of_birth)
        self.newsletter_checkbox.set_checked(user_data.signup_for_newsletter)
        self.offers_checkbox.set_checked(user_data.signup_for_offers)

        # Address Information
        self.first_name_input.fill(user_data.first_name)
        self.last_name_input.fill(user_data.last_name)
        self.company_input.fill(user_data.company)
        self.address_input.fill(user_data.address)
        self.address2_input.fill(user_data.address2)
        self.country_selector.select_option(user_data.country.value)
        self.state_input.fill(user_data.state)
        self.city_input.fill(user_data.city)
        self.zipcode_input.fill(user_data.zipcode)
        self.mobile_number_input.fill(user_data.mobile_number)

        self.create_account_button.click()
        return AccountCreatedPage(self.page)
