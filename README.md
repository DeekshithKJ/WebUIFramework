# Circula Task One Challenge - Test Automation Framework

This project is a test automation framework built using Selenium, pytest, and Python. The tests validate functionalities of the Circula application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Generating Test Reports](#generating-test-reports)
- [Browser Configuration](#browser-configuration)


## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- Node.js and npm (for managing `geckodriver`)
- Google Chrome browser
- Mozilla Firefox browser

## Project Structure

```plaintext
circula_task_one_framework/
│
├── tests/
│   └── test_country_dropdown.py  # Test cases
│
├── pages/
│   └── signup_page.py            # Page Object Model implementation
│
├── reports/                      # Folder where HTML test reports will be generated
│
├── conftest.py                   # Contains test configuration and fixtures
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation (this file)


## Setup and Installation

Clone the repository:

bash

git clone <your-repository-url>
cd circula_task_one_framework
Set up a Python virtual environment:

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required Python packages:

bash

Install geckodriver via npm:

bash

npm install geckodriver
Download and set up ChromeDriver:

Download the ChromeDriver that matches your Chrome version here.
Move the downloaded driver to a known location (e.g., Downloads/chromedriver).
Running Tests
To run the tests for both Chrome and Firefox:

bash

pytest --html=reports/report.html --self-contained-html
The tests are parameterized to run on both Chrome and Firefox browsers.

Running Tests for a Specific Browser
You can specify a browser by using:

bash

pytest --browser chrome  # For Chrome
pytest --browser firefox  # For Firefox
Generating Test Reports
The framework uses the pytest-html plugin to generate detailed HTML reports. After executing the tests, the report will be available at:


reports/report.html
Browser Configuration
The setup is designed to support both Chrome and Firefox with specific options configured for automation testing:

Chrome: Disables automation detection, runs in headless mode (optional), and disables info bars.
Firefox: Skips the default browser check and disables warning prompts on tab closure.
You can modify the configuration in the conftest.py file.

Notes:
Ensure that both chromedriver and geckodriver executables are properly set up and their paths are correctly configured in the conftest.py file.

If geckodriver is installed via npm, its path would typically be:

<your-project-directory>/node_modules/geckodriver/bin/geckodriver
If you encounter issues with browser drivers, ensure they are compatible with the installed browser versions.

