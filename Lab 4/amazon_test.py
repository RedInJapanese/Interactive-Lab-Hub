from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

api_key = "1E638B734DA64F17B4AAD4DA6A717ADF"
search_term = "Echo Dot 5th Generation"

url = "https://api.rainforestapi.com/request"
params = {
    "api_key": api_key,
    "type": "search",
    "amazon_domain": "amazon.com",
    "search_term": search_term
}

response = requests.get(url, params=params)
data = response.json()

# Extract ASINs from the search results
for product in data.get("search_results", []):
    title = product.get("title")
    asin = product.get("asin")
    print(f"{title}\nASIN: {asin}\n")


# Use Chrome so you can log in normally
driver = webdriver.Firefox()

# Open the product page
driver.get("https://www.amazon.com/dp/" + str(data.get("search_results", [])[0].get("asin")))

# Wait for page to load and log in manually if needed
time.sleep(10)

# Click "Add to Cart"
add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart.click()

print("✅ Item added to cart!")