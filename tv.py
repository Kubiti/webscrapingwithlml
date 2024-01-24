import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import time

def scrape_tv_data(url):
    # Send a GET request to the URL
    session = HTMLSession()
    response = session.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Wait for JavaScript to render the page
        response.html.render()

        # Give some time for the content to load (adjust as needed)
        time.sleep(5)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.html.html, 'html.parser')
        
        # Find the TV elements based on the HTML structure
        tv_elements = soup.find_all('div', class_='product__content')  # Adjust class name based on the actual HTML structure
        
        # Extract the name and price information
        tv_data = []
        for tv_element in tv_elements:
            name = tv_element.find('p', class_='product__description').text.strip()  # Adjust class name based on the actual HTML structure
            price = tv_element.find('span', class_='product__title').text.strip()  # Adjust class name based on the actual HTML structure
            tv_data.append({'name': name, 'price': price})
        
        tv_df = pd.DataFrame(tv_data)
        tv_df.to_csv('output.csv', index=False)
        return tv_data
        
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# Example URL (replace with the actual URL of the webpage containing TV information)
url = 'https://tonaton.com/c_tv-dvd-equipment'
result = scrape_tv_data(url)
print(result)
