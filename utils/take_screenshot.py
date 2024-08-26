import os
import time


def take_screenshot(driver, test_name):
    screenshots_dir = "reports/screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
