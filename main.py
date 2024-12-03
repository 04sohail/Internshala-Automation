import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

# Now you can perform actions on the website without encountering CAPTCHA
time.sleep(5)
print("Logged in successfully without CAPTCHA!")

# Close the browser
driver.quit()
