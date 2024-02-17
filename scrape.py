from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_tv_data(url):
    all_tv_data = []
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for JavaScript to render the page
    time.sleep(5)

    # Iterate through pages
    page_number = 52

    while True:
        # Find the TV elements based on the HTML structure
        
        # Check if there is a next page
        try:
            tv_number = 1
            while True:
                time.sleep(6)
                tv_elements = driver.find_elements(By.CSS_SELECTOR, '.product__content')  # Adjust CSS selector based on the actual HTML structure

                
                tv_element = tv_elements[tv_number]

                driver.execute_script("arguments[0].scrollIntoView(true);", tv_element)

                driver.execute_script("arguments[0].click();", tv_element)

                # Extract the name and price information
                time.sleep(6)
                details_description = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.details__description')))
                WebDriverWait(driver, 10).until(
                    EC.visibility_of(details_description)
                )                

                time.sleep(6)
                    #     # Extract additional details
                details_list = details_description.text.split('\n')
                # print('details_list', details_list)
                details_dict = {details_list[i + 1]: details_list[i] for i in range(0, len(details_list), 2)}
                # print(details_dict)
                name = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product__description'))).text
                price = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product__title'))).text

                # name = tv_element.find_element(By.CSS_SELECTOR, '.product__description').text.strip()
                # price = tv_element.find_element(By.CSS_SELECTOR, '.product__title').text.strip()
                # print('name', name, ' price', price)
                details_dict['name'] = name
                details_dict['price'] = price
                # print('details_dict', details_dict)
                print('details_dict tv', tv_number, details_dict)
                all_tv_data.append(details_dict)
            
                print('tv_number', tv_number,'page_number', page_number)
                tv_number += 1
                if (tv_number == len(tv_elements)):
                    driver.back()
                    time.sleep(6)
                    break
                # print('tv_number', tv_number)

                        # Go back to the main page
                # driver.execute_script("window.history.go(-1)")
                driver.back()
                time.sleep(6)


            print('page number', page_number)
            next_page_link = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.XPATH, f'//a[@href="/c_tv-dvd-equipment?page={page_number + 1}"]'))

            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_page_link)

            # next_page_link.click()
            driver.execute_script("arguments[0].click();", next_page_link)

            page_number += 1
            # if page_number == 3:
            #     break
            
        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()
            break  # Exit the loop if there is no next page or an error occurs

    driver.quit()

    # tv_df = pd.DataFrame(all_tv_data)
    # tv_df.to_csv('tv.csv', index=False)
    return all_tv_data

# Example URL (replace with the actual URL of the webpage containing TV information)
url = 'https://tonaton.com/c_tv-dvd-equipment?page=51'
# url = 'https://tonaton.com/c_tv-dvd-equipment'
result = scrape_tv_data(url)
print('result', result)
tv_df = pd.DataFrame(result)
tv_df.to_csv('tv3.csv', index=False)