# Update the import statement
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os

# Fixture for command-line options
def pytest_addoption(parser):
    parser.addoption("--sanity", action="store_true", help="Run tests in sanity mode")

@pytest.fixture(scope="session")
def sanity_mode(request):
    return request.config.getoption("--sanity")

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store_true", help="Run tests in sanity mode")

@pytest.fixture(scope="session")
def sanity_mode(request):
    return request.config.getoption("--base_url")

@pytest.fixture(scope="session")
def drivers():
    #If running on locale, uncomment this line, otherwise comment this line
    # chrome_driver_path = ChromeDriverManager().install()
    
    # Set the path to the Chrome binary
    chrome_options = Options()
    # Use the correct binary location for GitHub Actions
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable' #For Linux

    #If running on locale, uncomment this line, otherwise comment this line
    # chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'#For Mac
    # chrome_options.binary_location = 'c:/Program Files (x86)/Google/Chrome/Application/chrome.exe' #for windows
    
    download_directory = 'Downloads'
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    # Use headless mode for running in GitHub Actions (add other options if needed)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1200')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})
    

    # Create list to store WebDriver instances
    drivers = []
    try:
        # Set up ChromeDriver using the Service class
        ##If running on locale, uncomment this line, otherwise comment this line
        # service = Service(chrome_driver_path)
        #If running on github
        
        # Create four instances of Chrome WebDriver
        for _ in range(4):
            ##If running on locale, uncomment this line, otherwise comment this line
            # drivers.append(webdriver.Chrome(service=service, options=chrome_options))
            #If running on github
            drivers.append(webdriver.Chrome(options=chrome_options))
        
        # Yield the list of WebDriver instances to tests
        yield drivers
    finally:
        # Quit all WebDriver instances
        for driver in drivers:
            driver.quit()
