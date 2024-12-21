# Amazon Bestsellers Scraper 🛍️

A Python-based web scraping tool designed to extract detailed product information from Amazon's Bestsellers pages. The script supports multithreading for efficient data extraction and provides clean JSON output with minimal empty fields.

---

## 🚀 Features

- **Detailed Product Data Extraction**:
  - Product Title
  - Price
  - Sale Discount
  - Best Seller Rating
  - Customer Rating
  - Shipping and Seller Information
  - Description
  - Number of Purchases
  - Product Category
  - Product Images (with URLs)
- **Multithreaded Scraping**:
  - Utilizes Python's `concurrent.futures` for fast data collection.
- **Pagination Support**:
  - Automatically handles multiple pages of Amazon Bestsellers.
- **Error Handling**:
  - Ensures missing fields or parsing errors do not crash the script.
- **JSON Output**:
  - Saves the scraped data into a JSON file with a timestamped name.

---

## 📂 Project Structure

├── amazon_scraper.py        # Main script
├── output.json              # Python output files
├── README.md                # Project documentation

## 🛠️ Installation

### Clone the repository:

bash
git clone https://github.com/your-username/amazon-bestsellers-scraper.git

##🔧 Usage
Run the script:
bash
Copy code
python amazon_scraper.py
Provide the URL of the Amazon Bestsellers page when prompted:
plaintext
Copy code
Enter the URL of the Amazon Bestsellers page: https://www.amazon.in/gp/bestsellers
The script will scrape product details and save the results in a JSON file in the output/ directory with a timestamped name:
plaintext
Copy code
amazon_bestsellers.json

📊 JSON Output Example
json
Copy code
[
    {
        "Title": "Sample Product",
        "Price": "999",
        "Sale Discount": "10%",
        "Best Seller Rating": "4.5 out of 5 stars",
        "Rating": "4.5",
        "Ship From": "Amazon",
        "Sold By": "ABC Seller",
        "Description": "This is a sample description.",
        "Number Bought": "100 bought in the past month",
        "Category": "Electronics",
        "Images": [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg"
        ]
    }
]

##⚙️ Configuration
Default Settings:
Maximum number of products: 50
Headers: Custom User-Agent to mimic a browser request.
To change the maximum number of products scraped, update the max_products variable in the script.

##🧩 Dependencies
This project requires Python 3.7 or higher and the following libraries:

beautifulsoup4 - For parsing HTML content.
requests - For sending HTTP requests.
pandas - (Optional) For potential data manipulation.
concurrent.futures - For multithreading.
json - For working with JSON data.
