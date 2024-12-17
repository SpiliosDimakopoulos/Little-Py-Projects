#This code no longer works for most users: This browser or app may not be secure.
#this issue happens only in a scenario when multiple gmail accounts have already been created from the same App/IP/Device.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromedriver_path = "Enter Your Driver"
gmailId = 'enteryouremail@gmail.com'
passWord = 'enter-your-password'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the Google Sign-In page
    driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&amp;service=mail&amp;sacu=1&amp;rip=1&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin')
    driver.implicitly_wait(15)

    # Enter the Gmail ID
    loginBox = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    loginBox.send_keys(gmailId)

    # Click the 'Next' button
    nextButton = driver.find_element(By.XPATH, '//*[@id="identifierNext"]')
    nextButton.click()

    # Wait for password field to be present
    driver.implicitly_wait(15)

    # Enter the password
    passWordBox = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    passWordBox.send_keys(passWord)

    # Click the 'Next' button
    nextButton = driver.find_element(By.XPATH, '//*[@id="passwordNext"]')
    nextButton.click()

    print('Login Successful...!!')
except Exception as e:
    print('Login Failed:', str(e))
finally:
    # Close the browser
    driver.quit()
