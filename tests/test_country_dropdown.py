import time

import pytest
from pages.signup_page import SignUpPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestCountryDropdown:
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def test_sweden_is_in_dropdown(self):
        signup_page = SignUpPage(self.driver)
        signup_page.dismiss_consent_overlay()

        # Click on the input field to trigger the dropdown
        country_input = self.driver.find_element(By.CSS_SELECTOR, "#registration-country-input")
        country_input.click()

        # Wait for the dropdown options to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul#registration-country-menu"))
        )

        # Improved JavaScript selector and interaction script
        js_script = """
            let dropdown = document.querySelector('ul#registration-country-menu');
            if (dropdown) {
                dropdown.style.display = 'block'; // Force display if hidden
                const options = dropdown.querySelectorAll('li'); // Adjusted selector
                for (let option of options) {
                    if (option.textContent.includes('Sweden')) {
                        option.click(); // Click on Sweden
                        return true;
                    }
                }
            }
            return false; // Return false if not found
        """

        is_sweden_in_dropdown = self.driver.execute_script(js_script)

        # Assert that Sweden is present in the dropdown
        assert is_sweden_in_dropdown, "Sweden is not found in the dropdown"

    def test_select_sweden_and_submit(self):
        signup_page = SignUpPage(self.driver)
        signup_page.select_country("Sweden")

        signup_page.submit_form()
        assert "Please explain, how you discovered Circula." in signup_page.get_confirmation_message()

    def test_alphabetical_order(self):
        signup_page = SignUpPage(self.driver)
        signup_page.select_country("")  # Trigger the dropdown without any input

        # Implement logic to extract all countries from the dropdown and validate alphabetical order
        country_elements = self.driver.find_elements(By.XPATH, "//ul[@id='registration-country-menu']//li")
        countries = [country.text for country in country_elements]
        print(countries)

        assert countries == sorted(countries), "The countries are not in alphabetical order"

    def test_invalid_email(self):
        signup_page = SignUpPage(self.driver)
        invalid_email = "invalid-email-format@"
        signup_page.enter_email(invalid_email)
        signup_page.submit_form()
        error_message = signup_page.get_error_message()
        assert "Please correct the e-mail address." in error_message, "Error message not displayed for invalid email"

    def test_invalid_phone_number(self):
        signup_page = SignUpPage(self.driver)
        invalid_phone = "123abc"
        signup_page.enter_phone_number(invalid_phone)
        signup_page.submit_form()
        error_message = signup_page.get_error_message()
        assert "Please enter a valid phone number" in error_message, "Error message not displayed for invalid phone number"
