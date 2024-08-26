import platform
from lib2to3.pgen2 import driver

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://app.circula.com/users/sign_up")

    def dismiss_consent_overlay(self):
        try:
            # Locate the shadow host element
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#usercentrics-root"))
            )
            # Access the shadow DOM
            shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
            consent_button = shadow_root.find_element(By.CSS_SELECTOR, ".sc-dtBdUo.fzvttm")
            if consent_button:
                consent_button.click()
        except Exception as e:
            print(f"Consent overlay not found or not interactable. Continuing with the test. Error: {e}")

    def select_country(self, country_name):
        self.dismiss_consent_overlay()
        self.clear_country_input()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='registration-country-input']"))
        ).click()
        country_input = self.driver.find_element(By.XPATH, "//input[@id='registration-country-input']")
        country_input.clear()
        country_input.send_keys(country_name)

    def clear_country_input(self):
        """Clears the country input field using Ctrl + A and Delete keys."""
        country_input = self.driver.find_element(By.ID, "registration-country-input")

        # Use Ctrl + A (Command + A on Mac) and Delete
        if platform.system() == 'Darwin':  # For Mac
            country_input.send_keys(Keys.COMMAND + "a")
        else:  # For Windows/Linux
            country_input.send_keys(Keys.CONTROL + "a")
        country_input.send_keys(Keys.DELETE)

    def submit_form(self):
        # Logic to submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    def get_confirmation_message(self):
        """Fetch the confirmation message after form submission."""
        try:
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/form[1]/label[1]/div[3]/div[1]"))
            )
            return confirmation_message.text
        except Exception as e:
            print(f"Error while fetching confirmation message: {e}")
            return None

    country_locator = (By.ID, "registration-country-input")

    def read_country_list(self):
        country_elements = self.driver.find_elements(By.ID, "registration-country-input")
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.country_locator)
        )
        options = dropdown.find_elements(By.TAG_NAME, "li")
        is_sweden_present = any("Sweden" in option.text for option in options )

        print(f"Sweden present: {is_sweden_present}")


    email_input_locator = (By.XPATH, '(//input[@id="textfield-:Rjmkmm:"])[1]')
    phone_number_input_locator = (By.XPATH, '//input[@id="textfield-:R13mkmm:"]')
    error_message_locator =  (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/form[1]/div[3]/label[1]/div[3]/div[1]")

    def enter_email(self, email):
        email_input = self.driver.find_element(*self.email_input_locator)
        email_input.clear()
        email_input.send_keys(Keys.CONTROL + "a")  # Select all
        email_input.send_keys(Keys.DELETE)  # Clear existing input
        email_input.send_keys(email)

    def enter_phone_number(self, phone_number):
        phone_input = self.driver.find_element(*self.phone_number_input_locator)
        phone_input.clear()
        phone_input.send_keys(Keys.CONTROL + "a")  # Select all
        phone_input.send_keys(Keys.DELETE)  # Clear existing input
        phone_input.send_keys(phone_number)

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message_locator)
        ).text

    def clear_input_fields(self):
        """Clears both email and phone number fields using Ctrl + A (or Command + A on Mac) and Delete."""
        email_input = self.driver.find_element(*self.email_input_locator)
        phone_input = self.driver.find_element(*self.phone_number_input_locator)

        if platform.system() == 'Darwin':  # For Mac
            email_input.send_keys(Keys.COMMAND + "a")
            phone_input.send_keys(Keys.COMMAND + "a")
        else:  # For Windows/Linux
            email_input.send_keys(Keys.CONTROL + "a")
            phone_input.send_keys(Keys.CONTROL + "a")

        email_input.send_keys(Keys.DELETE)
        phone_input.send_keys(Keys.DELETE)

    first_name_locator = (By.XPATH, "(// input[@ id='textfield-:Rimkmm:'])[1]")
    last_name_locator = (By.XPATH, "(//input[@id='textfield-:R12mkmm:'])[1]")
    password_locator = (By.XPATH, "(//input[@id='textfield-:R2kmkmm:'])[1]")
    company_name_locator = (By.XPATH, "(//input[@id='textfield-:R14mkmm:'])[1]")
    comment_box_locator = (By.XPATH, "(//textarea[@id='textfield-:R6mkmm:'])[1]")
    agree_button_locator = (By.XPATH, "//div[@role='alert']//preceding::input[@type='checkbox' and contains(@id, 'terms')]")

    def enter_first_name(self, firstname):
        firstname_input = self.driver.find_element(*self.first_name_locator)
        firstname_input.clear()
        firstname_input.send_keys(Keys.CONTROL + "a")  # Select all
        firstname_input.send_keys(Keys.DELETE)  # Clear existing input
        firstname_input.send_keys(firstname)


    def enter_last_name(self, lastname):
        lastname_input = self.driver.find_element(*self.last_name_locator)
        lastname_input.clear()
        lastname_input.send_keys(Keys.CONTROL + "a")  # Select all
        lastname_input.send_keys(Keys.DELETE)  # Clear existing input
        lastname_input.send_keys(lastname)


    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_locator)
        password_input.clear()
        password_input.send_keys(Keys.CONTROL + "a")  # Select all
        password_input.send_keys(Keys.DELETE)  # Clear existing input
        password_input.send_keys(password)

    def enter_comment_box(self, comment):
        comment_input = self.driver.find_element(*self.comment_box_locator)
        comment_input.clear()
        comment_input.send_keys(Keys.CONTROL + "a")  # Select all
        comment_input.send_keys(Keys.DELETE)  # Clear existing input
        comment_input.send_keys(comment)

    def enter_company_name(self, companyname):
        company_input = self.driver.find_element(*self.company_name_locator)
        company_input.clear()
        company_input.send_keys(Keys.CONTROL + "a")  # Select all
        company_input.send_keys(Keys.DELETE)  # Clear existing input
        company_input.send_keys(companyname)

    def click_agree_button(self):
        agree_btn = self.driver.find_element(*self.agree_button_locator)
        driver.execute_script("arguments[0].scrollIntoView();", agree_btn)
        driver.execute_script("arguments[0].click();", agree_btn)





