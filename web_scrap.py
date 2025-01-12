import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

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
    
    job_tiles = driver.find_elements(By.CSS_SELECTOR, "article.job-tile")
    
    jobs = []
    for job_tile in job_tiles:
        title_element = job_tile.find_element(By.CSS_SELECTOR, "h2.job-tile-title a")
        description_element = job_tile.find_element(By.CSS_SELECTOR, "p.mb-0.text-body-sm")
        tags_elements = job_tile.find_elements(By.CSS_SELECTOR, "div.air3-token-container span")
        fixed_price_element = job_tile.find_element(By.CSS_SELECTOR, "li[data-test='experience-level'] strong")

        est_budget_element = None
        if job_tile.find_elements(By.CSS_SELECTOR, "li[data-test='is-fixed-price'] strong:nth-of-type(2)"):
            est_budget_element = job_tile.find_element(By.CSS_SELECTOR, "li[data-test='is-fixed-price'] strong:nth-of-type(2)")
        elif job_tile.find_elements(By.CSS_SELECTOR, "li[data-test='duration-label'] strong:nth-of-type(2)"):
            est_budget_element = job_tile.find_element(By.CSS_SELECTOR, "li[data-test='duration-label'] strong:nth-of-type(2)")
        
        posted_date_element = job_tile.find_element(By.CSS_SELECTOR, "small.text-light.mb-1 span:last-child")
        
        tags = [tag.text for tag in tags_elements]
        fixed_price = fixed_price_element.text if fixed_price_element else "N/A"
        est_budget = est_budget_element.text if est_budget_element else "N/A"
        posted_date = posted_date_element.text if posted_date_element else "N/A"

        jobs.append({
            "title": title_element.text,
            "description": description_element.text,
            "tags": tags,
            "fixed_price": fixed_price,
            "est_budget": est_budget,
            "posted_date": posted_date
        })
    
    print(json.dumps(jobs))

finally:
    driver.quit()
