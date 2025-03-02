from selenium import webdriver
from selenium.webdriver.common.by import By
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
driver.get("https://www.bstackdemo.com/")
# Extract product data
products = driver.find_elements(By.CLASS_NAME, "shelf-item__title")
for product in products:
    print(product.text)


driver.quit()
