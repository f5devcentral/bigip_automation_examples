"""Waffler library for some of needed functions."""

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# some of element locators and urls
site_url = 'https://waffler.dev/rc'
policy_name_xpath = "// input[ @ value = 'policy_name']"
language_xpath = "// input[ @ value = 'utf-8']"
mode_xpath = "// input[ @ value = 'blocking']"
template_name_xpath = "// input[ @ value = 'POLICY_TEMPLATE_NGINX_BASE']"
download_xpath = "//span[text()='Download']"
json_view_xpath = "//*[@class='npm__react-simple-code-editor__textarea']"


def open_waffler_site(browser='chrome', remote=False, headless=True, remoteip='localhost', remoteport='4444'):
    """Open waffler site using provided browsers."""
    logging.info("Opening waffler.")
    print("================ Opening waffler ==================")
    driver = ""
    prefs = {'download.default_directory': 'C:\\waffler_downloads'}
    if remote:
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_experimental_option('prefs', prefs)
            capabilities = options.to_capabilities()
            driver = webdriver.Remote(command_executor='http://{0}:{1}/wd/hub'.format(remoteip, remoteport),
                                      desired_capabilities=capabilities)
    elif browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', prefs)
        if headless:
            chrome_options.headless = headless
        driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
        driver.set_window_size(1500, 900)
    elif browser == 'firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.panel.shown", False)
        profile.set_preference("browser.helperApps.neverAsk.openFile", "application/json")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.folderList", 1)
        profile.set_preference("browser.altClickSave", True)
        driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(site_url)
    driver.maximize_window()
    return driver


def validate_title(title, driver):
    """Validate if title is correct."""
    logging.info("Validating title.")
    print("================ Validating title ==================")
    assert title in driver.title


def clear_input(ui_element):
    """Clear existing input for an element."""
    logging.info("Clearing element input.")
    print("================ Clearing input value. ==================")
    ui_element.send_keys(Keys.CONTROL + "a")
    ui_element.send_keys(Keys.DELETE)


def validate_element_enabled(ui_element, enabled=True):
    """Validate if provided element is disabled."""
    logging.info("Validating if element is enabled/disabled.")
    print("======== Validating if button is enabled/disabled ========")
    print(ui_element.is_enabled())
    if enabled:
        assert ui_element.is_enabled()
    else:
        assert not ui_element.is_enabled()


def get_policy_name_element(driver):
    """Return policy name element."""
    logging.info("Returning policy name element.")
    print("======== Returning policy name element. ==============")
    return driver.find_element_by_xpath(policy_name_xpath)


def get_language_element(driver):
    """Return language element."""
    logging.info("Returning language element.")
    print("================ Returning language element. ==================")
    return driver.find_element_by_xpath(language_xpath)


def get_mode_element(driver):
    """Return mode element."""
    logging.info("Returning policy mode element.")
    print("================ Returning policy mode element. ==================")
    return driver.find_element_by_xpath(mode_xpath)


def get_template_name_element(driver):
    """Return template name element."""
    logging.info("Returning template name element.")
    print("================ Returning template name element. ==================")
    return driver.find_element_by_xpath(template_name_xpath)


def download_json(driver, browser='chrome'):
    """Lib to download json file."""
    logging.info("Downloading json file.")
    print("================ Downloading json file. ==================")
    download_button = driver.find_element_by_xpath(download_xpath)
    if browser == 'chrome':
        driver.execute_script("arguments[0].click();", download_button)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.get_screenshot_as_file("downloaded_json.jpg")
    elif browser == 'firefox':
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
    time.sleep(2)


def get_view_json(driver):
    """Lib to get editable area of json file."""
    return driver.find_element_by_xpath(json_view_xpath)


def validate_input(ui_element, value):
    """Validate provided value for an element."""
    logging.info("Validating input value is valid or not.")
    print("======== Validating input value is valid or not. =========")
    assert ui_element
    assert value
