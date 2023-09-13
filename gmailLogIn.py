#import required package
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Path of the chromedriver.exe file
ser_obj = Service("H:/software/driver2/chromedriver.exe")

# Create an instance of the Chrome WebDriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options,service=ser_obj)


# Navigate to the sample web application's login page
driver.get("https://www.gmail.com")

#maximize the window
driver.maximize_window()

# Find the username input fields by their HTML attributes
search=driver.find_element(By.NAME,'identifier')

# Input the username
search.send_keys('jashosa@gmail.com')

# Find the click next button fields by their HTML attributes
gmail_next=driver.find_element(By.XPATH,"//span[contains(text(), 'Next')]")

# Click the next button to submit the user name
gmail_next.click()

# Find the password input fields  by their HTML attributes
password=driver.find_element(By.CLASS_NAME,'whsOnd zHQkBf')

# Input the password
password.send_keys('User12345*')

# Find the click next button fields by their HTML attributes
password_next=driver.find_element(By.XPATH,"//*[@id="passwordNext"]/div/button/span")

# Click the next button to submit the password
password_next.click()

# Close the browser window
driver.quit()


