from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()  # Assuming ChromeDriver is in PATH

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)  # Wait for page to load

        # Handle cookie popup
        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Accept All Cookies')]").click()
        except:
            pass
        
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

        # Handle save login info popup if it appears
        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            pass

        # Handle turn on notifications popup if it appears
        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            pass

    def search_user_or_topic(self, query):
        try:
            # Navigate to explore page
            self.driver.get("https://www.instagram.com/explore/")
            time.sleep(3)  # Wait for page to load
        except:
            pass
        
        try:
            # Enter the search query
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
            search_input.send_keys(query)
            time.sleep(2)  # Wait for search results to load

            # Click on the first search result
            first_search_result = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='fuqBx']//a"))
            )
            first_search_result.click()
            print(f"Searched for '{query}'")
        except Exception as e:
            print("Error:", e)
            pass

    def quit(self):
        self.driver.quit()

# Example usage:
bot = InstagramBot("REPLACE USERNAME", "REPLACE PASSWORD")
bot.login()
bot.search_user_or_topic("REPLACE SEARCH")
bot.quit()
