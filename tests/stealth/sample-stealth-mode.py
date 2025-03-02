from selenium import webdriver
from selenium_stealth import stealth

# create ChromeOptions object
options = webdriver.ChromeOptions()
options.add_argument('--headless')

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
driver.get("https://opensea.io/")
print(driver.execute_script("return navigator.webdriver"))  # Should return None
print(driver.title)

driver.quit()
