from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def get_driver():
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    
    # Basic options
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    
    # SSL and security options
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Automation options
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # Automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=options)
    
    # Get absolute path to HTML file
    file_path = os.path.abspath("index.html")
    print(f"\n🔄 Loading practice page from:\n{file_path}\n")
    driver.get(f"file:///{file_path}")
    return driver

def scrape_products(driver):
    print("🛍️ Found Products:")
    products = driver.find_elements(By.CSS_SELECTOR, ".product")
    for product in products:
        name = product.find_element(By.TAG_NAME, "h3").text
        price = product.find_element(By.CLASS_NAME, "price").text
        print(f"- {name} ({price})")
    return len(products)

def main():
    driver = None
    try:
        driver = get_driver()
        time.sleep(1)  # Brief pause for page load
        
        # Count and display products
        product_count = scrape_products(driver)
        print(f"\n✅ Successfully scraped {product_count} products\n")
        
        return product_count
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}\n")
        return 0
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()