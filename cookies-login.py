import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Path to save/load cookies
COOKIE_FILE = "cookies.pkl"

# Initialize WebDriver (not headless mode)
driver = webdriver.Chrome()

# Open Internshala
driver.get("https://internshala.com")

# Wait for the page to load
time.sleep(3)

# Load cookies if they exist
try:
    with open(COOKIE_FILE, "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
    print("Cookies loaded successfully!")
except FileNotFoundError:
    print("No cookies found. Please log in manually first.")

# Refresh the page to keep the session alive after loading cookies
driver.refresh()

# Wait to confirm the login is successful
time.sleep(5)

# Check if logged in successfully by looking for an element that appears only when logged in
try:
    driver.find_element(By.CLASS_NAME, "user_profile")  # Adjust according to Internshala's UI
    print("Logged in successfully using saved cookies!")
except:
    print("Login failed! Please check cookies or log in manually.")

# Proceed with the automation tasks (e.g., applying for internships)
# You can now interact with the website (e.g., apply for internships) using the session

# Example action: Go to the internships page
driver.get("https://internshala.com/internships")

# Add your automation tasks here
# For example, you can scrape internships or apply for internships

# Close the browser after completing tasks
driver.quit()