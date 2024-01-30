# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_product_details(url):
    # Set up the Selenium WebDriver (replace 'path_to_chromedriver' with the actual path)
    driver = webdriver.Chrome()
    # driver.get(url)
    try:
        # Open the URL
        driver.get(url)

        details_description = WebDriverWait(driver, 500).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'details__description'))
        ).text
        # print(details_description.text)
        # children = details_description.find_elements(By.XPATH, ".//*")
        details_list = details_description.split('\n')
        details_dict = {details_list[i + 1]: details_list[i] for i in range(0, len(details_list), 2)}

        print(details_dict)
        # Print the text content of each child
        # for child in children:
        #     print(child.text)

        # # Extract details
        # brand = details_description.find_element(By.XPATH, ".//p[text()=' Brand ']").text
        # model = details_description.find_element(By.XPATH, ".//p[text()='Model']/following-sibling::p").text
        # product_type = details_description.find_element(By.XPATH, ".//p[text()='Type']/following-sibling::p").text
        # screen_size = details_description.find_element(By.XPATH, ".//p[text()='Screen Size']/following-sibling::p").text
        # display_technology = details_description.find_element(By.XPATH, ".//p[text()='Display Technology']/following-sibling::p").text
        # condition = details_description.find_element(By.XPATH, ".//p[text()='Condition']/following-sibling::p").text

        # Print or store the scraped details
        # print("Brand:", brand)
        # print("Model:", model)
        # print("Type:", product_type)
        # print("Screen Size:", screen_size)
        # print("Display Technology:", display_technology)
        # print("Condition:", condition)

    finally:
        # Close the browser window
        driver.quit()

# Example usage
url = "https://tonaton.com/a_be-at-comfort-call-and-order-hg32ae690dk-fhd-satellite-32-tv-grtjrOtgfDYoh8HwKt65gTtO.html"
scrape_product_details(url)
