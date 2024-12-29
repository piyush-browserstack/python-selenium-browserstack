from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_test(driver):
    """Function to execute the test"""
    try:
        # Open the target website
        driver.get('https://bstackdemo.com/')
        
        # Wait for the page title to contain 'StackDemo'
        WebDriverWait(driver, 10).until(EC.title_contains('StackDemo'))
        
        # Get the text of the product - iPhone 12
        item_on_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))
        ).text
        
        # Click the 'Add to cart' button if it is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]'))
        ).click()
        
        # Check if the Cart pane is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'float-cart__content'))
        )
        
        # Get the text of the product in the cart
        item_in_cart = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))
        ).text
        
        # Verify whether the product (iPhone 12) is added to the cart
        if item_on_page == item_in_cart:
            print(f"Test Passed: iPhone 12 successfully added to cart on {driver.name}!")
        else:
            print(f"Test Failed: iPhone 12 not added to cart on {driver.name}!")
    except NoSuchElementException as e:
        print(f"Test Failed on {driver.name}: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed on {driver.name}: Operation timed out - {e}")
    except Exception as e:
        print(f"Test Failed on {driver.name}: An unexpected error occurred - {e}")
    finally:
        # Stop the driver
        driver.quit()

# Run on Chrome
chrome_driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
print("Running test on Chrome...")
run_test(chrome_driver)

# Run on Safari
try:
    safari_driver = webdriver.Safari()  # SafariDriver is pre-installed on macOS
    print("Running test on Safari...")
    run_test(safari_driver)
except Exception as e:
    print(f"Safari test could not run: {e}")

# Run on Firefox
firefox_driver = webdriver.Firefox()  # Ensure GeckoDriver is installed and in PATH
print("Running test on Firefox...")
run_test(firefox_driver)