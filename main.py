from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WhatsApp Web URL
whatsapp_url = "https://web.whatsapp.com/"

# Initialize WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get(whatsapp_url)

# Wait for QR code scan
print("Please scan the QR code")
time.sleep(15)  # Adjust sleep time as needed for QR code scan

# Locate status button and click
status_button = driver.find_element(By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[1]/div')
status_button.click()

# Wait for statuses to load
time.sleep(5)

# Retrieve and print status
statuses = driver.find_elements(By.CLASS_NAME, 'status-list-item')
for status in statuses:
    status.click()
    time.sleep(2)  # Adjust sleep time as needed for viewing status

driver.quit()
