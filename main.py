import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Path to save and load cookies
COOKIE_FILE = "cookies.pkl"

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Internshala login page
driver.get("https://internshala.com")

# Check if cookies file exists and load cookies
try:
    driver.get("https://internshala.com")
    with open(COOKIE_FILE, "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
    print("Cookies loaded successfully!")
except FileNotFoundError:
    print("No cookies found. Please log in manually first.")
    # Wait for the user to log in manually
    input("Please log in manually, then press Enter here to continue...")

# Refresh the page after cookies are loaded to keep the session active
driver.refresh()
time.sleep(5)
print("Logged in successfully without CAPTCHA!")

# Locate the "Internships" menu item to hover
try:
    internships_menu = driver.find_element(By.LINK_TEXT, "Internships")  # Adjust the locator if necessary

    # Use ActionChains to hover over the "Internships" menu
    actions = ActionChains(driver)
    actions.move_to_element(internships_menu).perform()
    print("Hovered over 'Internships' menu.")

    # Wait for the dropdown menu to appear and click "View All Internships"
    view_all_internships = driver.find_element(By.LINK_TEXT, "View all internships")  # Adjust locator if necessary
    view_all_internships.click()
    print("Navigated to 'View All Internships' page.")

    # Wait for the page to load
    time.sleep(5)

except Exception as e:
    print("Error navigating to 'View All Internships':", e)

# Close the browser
driver.quit()
