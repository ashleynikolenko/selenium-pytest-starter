from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_python_search():
    # Set Chrome options
    options = Options()
    options.add_argument("--headless=new")   # Run headless so no browser window pops up
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start Chrome (Selenium Manager will fetch the right ChromeDriver automatically)
    driver = webdriver.Chrome(options=options)

    try:
        # Open python.org
        driver.get("https://www.python.org/")

        # Check the page title
        assert "Python" in driver.title

        # Interact with the search box
        search_box = driver.find_element(By.ID, "id-search-field")
        search_box.clear()
        search_box.send_keys("pytest")
        search_box.submit()

        # Check that results exist
        results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events.menu li")
        assert len(results) > 0, "No search results found on python.org"
    finally:
        driver.quit()
