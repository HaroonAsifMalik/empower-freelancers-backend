from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def retry_request(driver, max_retries=5, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            driver.get("https://www.upwork.com/nx/search/jobs/?q=django")
            return
        except Exception as e:
            retries += 1
            wait_time = delay * (2 ** retries)
            print(f"Error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

options = webdriver.ChromeOptions()

options.binary_location = "/usr/local/bin/chromium"

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.headless = True

driver = webdriver.Chrome(options=options)

try:
    retry_request(driver)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.job-tile"))
    )
    job_titles = driver.find_elements(By.CSS_SELECTOR, "h2.job-tile-title a")
    job_descriptions = driver.find_elements(By.CSS_SELECTOR, "p.mb-0.text-body-sm")
    for title, description in zip(job_titles, job_descriptions):
        print(f"Job Title: {title.text}")
        print(f"Description: {description.text}")
        print("-" * 40)

finally:
    driver.quit()