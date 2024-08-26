import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def setup(request):
    browser = request.param
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--headless") #remove this line if you wish to see the execution on the browser window
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Update the path to your locally installed ChromeDriver
        service = ChromeService(
            executable_path="/Users/deekshithkrishnapurajayakumar/Downloads/chromedriver_mac64_New/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("browser.startup.homepage_override.mstone", "ignore")
        firefox_options.set_preference("browser.startup.page", 0)  # Skip the default browser check
        firefox_options.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        firefox_options.set_preference("browser.tabs.warnOnClose", False)
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        # Update the path to your locally installed GeckoDriver
        service = FirefoxService(executable_path="/Users/deekshithkrishnapurajayakumar/Downloads/Geckodriver_mac64/geckodriver")
        driver = webdriver.Firefox(service=service, options=firefox_options)

    request.cls.driver = driver
    yield driver
    driver.quit()
