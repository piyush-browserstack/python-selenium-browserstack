import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Define a pytest fixture for the WebDriver setup and teardown
@pytest.fixture(params=["chrome", "firefox", "safari"], scope="function")
def driver(request):
    """Fixture to initialize and clean up the WebDriver."""
    if request.param == "chrome":
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
    elif request.param == "firefox":
        driver = webdriver.Firefox()  # Ensure GeckoDriver is installed and in PATH
    elif request.param == "safari":
        driver = webdriver.Safari()  # SafariDriver is pre-installed on macOS
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    yield driver  # This provides the driver instance to the test
    driver.quit()  # Quit the driver after the test completes

def test_add_to_cart(driver):
    """Test to verify adding a product to the cart."""
    try:
        # Open the target website
        driver.get('https://bstackdemo.com/')
        
        # Wait for the page title to contain 'StackDemo'
        WebDriverWait(driver, 30).until(EC.title_contains('StackDemo'))
        # Get the text of the product - iPhone 12
        item_on_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))
        ).text
        
        # Click the 'Add to cart' button if it is visible
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]'))
        ).click()
        
        # Check if the Cart pane is visible
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'float-cart__content'))
        )
        # Get the text of the product in the cart
        item_in_cart = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))
        ).text
        
        # Verify whether the product (iPhone 12) is added to the cart
        assert item_on_page == item_in_cart, f"Expected item: {item_on_page}, but found: {item_in_cart}"
        print(f"Test Passed: iPhone 12 successfully added to cart on {driver.name}!")
    except NoSuchElementException as e:
        pytest.fail(f"Test Failed on {driver.name}: Element not found - {e}")
    except TimeoutException as e:
        pytest.fail(f"Test Failed on {driver.name}: Operation timed out - {e}")
    except Exception as e:
        pytest.fail(f"Test Failed on {driver.name}: An unexpected error occurred - {e}")
