import time
from bs4 import BeautifulSoup
import requests
import json
from concurrent.futures import ThreadPoolExecutor

# Headers for the request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Function to fetch product details from a product page
def fetch_product_details(product_url):
    try:
        new_webpage = requests.get(product_url, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        # Extract details with proper fallback to None
        title = new_soup.find("span", attrs={"id": 'productTitle'})
        price = new_soup.find("span", attrs={"class": 'a-price-whole'})
        sale_discount = new_soup.find("span", attrs={"class": 'a-color-price'})
        rating = new_soup.find("span", attrs={"class": 'a-icon-alt'})
        best_seller_rating = new_soup.find("span", attrs={"id": 'acrPopover'})
        ship_from = new_soup.find("span", text="Ships from")
        sold_by = new_soup.find("span", text="Sold by")
        description = new_soup.find("div", attrs={"id": 'productDescription'})
        num_bought = new_soup.find("span", text="bought in the past month")
        category = new_soup.find("a", attrs={"class": 'a-link-normal a-color-tertiary'})

        # Parse values and fallback to None if not found
        return {
            "Title": title.text.strip() if title else None,
            "Price": price.text.strip() if price else None,
            "Sale Discount": sale_discount.text.strip() if sale_discount else None,
            "Best Seller Rating": best_seller_rating.get('title') if best_seller_rating else None,
            "Rating": rating.text.strip() if rating else None,
            "Ship From": ship_from.find_next("span").text.strip() if ship_from else None,
            "Sold By": sold_by.find_next("span").text.strip() if sold_by else None,
            "Description": description.text.strip() if description else None,
            "Number Bought": num_bought.text.strip() if num_bought else None,
            "Category": category.text.strip() if category else None,
        }
    except Exception as e:
        return None  # Return None if an error occurs

# Function to get product links from a page
def get_product_links(page_url):
    try:
        webpage = requests.get(page_url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        links = soup.find_all("a", attrs={'class': 'a-link-normal'})
        product_links = ["https://www.amazon.in" + link.get('href') for link in links if link.get('href')]
        return list(set(product_links))  # Remove duplicates
    except Exception as e:
        return []

# Function to scrape all product details concurrently
def scrape_amazon_bestsellers(base_url):
    product_data = []
    max_products = 50
    products_fetched = 0
    page_number = 1
    
    while products_fetched < max_products:
        page_url = f"{base_url}?page={page_number}"
        product_links = get_product_links(page_url)
        
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(fetch_product_details, product_links[:max_products - products_fetched]))
        
        # Filter out None or incomplete data
        results = [product for product in results if product and any(product.values())]
        
        product_data.extend(results)
        products_fetched += len(results)
        page_number += 1

        if len(product_links) == 0:  # Stop if no more links found
            break

    return product_data

# Main script execution
if __name__ == "__main__":
    # Get user input for URL
    user_url = input("Enter the URL of the Amazon Bestsellers page: ").strip()
    
    # Fetch product data
    product_data = scrape_amazon_bestsellers(user_url)
    
    # Generate unique file name with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_name_json = f"amazon_bestsellers_{timestamp}.json"
    
    # Save data to JSON
    with open(file_name_json, 'w', encoding='utf-8') as json_file:
        json.dump(product_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Data saved to {file_name_json}")
