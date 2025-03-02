from selenium import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent

# Generate a random User-Agent
user_agent = UserAgent().random


# create ChromeOptions object
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument(f"user-agent={user_agent}")

# Set up WebDriver
driver = webdriver.Chrome(options=options)

# Apply stealth mode
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True, 
        webdriver = False)

# Open a webpage
driver.get("https://www.whatismybrowser.com/")
print(f"Using User-Agent: {user_agent}")


driver.quit()
