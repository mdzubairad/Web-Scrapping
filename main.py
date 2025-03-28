from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # Automatically download and use the correct ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    file_path = os.path.abspath("index.html")
    driver.get(f"file:///{file_path}")
    return driver

def main():
    driver = get_driver()
    try:
        element = driver.find_element("xpath", "/html/body/section[1]/div[1]/p[2]")
        return element.text
    finally:
        driver.quit()

if __name__ == "__main__":
    print(main())