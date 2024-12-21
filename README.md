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
git clone https://github.com/jdesai05/amazon-bestsellers-scraper.git
