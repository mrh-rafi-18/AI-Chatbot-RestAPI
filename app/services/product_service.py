import requests
from app.core.config import settings
from langchain_core.tools import tool

def fetch_all_products():
    """Fetch all products from DummyJSON API."""
    response = requests.get(settings.DUMMYJSON_API_URL)
    response.raise_for_status()
    return response.json()


BASE_URL = settings.DUMMYJSON_API_URL


fields_to_keep = [
    "id", "title", "description", "category", "price", 
    "discountPercentage", "rating", "stock", "tags", "brand", 
    "weight", "warrantyInformation", "shippingInformation", 
    "availabilityStatus", "returnPolicy", "minimumOrderQuantity"
]



"""A collection of tools to interact with the DummyJSON Products API."""

# ========== BASIC TOOLS ==========


@tool
def get_product_by_id(product_id: int):
    """Fetch details of a specific product by its ID."""
    url = f"{BASE_URL}/{product_id}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return {"error": f"Product with ID {product_id} not found"}

@tool
def search_product(query: str):
    """Search for products using a keyword (e.g., 'phone', 'laptop')."""
    url = f"{BASE_URL}/search?q={query}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return {"error": f"No results found for query '{query}'"}

@tool
def get_products_by_category(category: str):
    """Get all products from a specific category (e.g., 'beauty', 'groceries')."""
    url = f"{BASE_URL}/category/{category}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return {"error": f"No products found in category '{category}'"}

# ========== PRODUCT DETAILS TOOLS ==========

@tool
def get_product_reviews(product_name: str):
    """Get reviews for a specific product."""
    url = f"{BASE_URL}/search?q={product_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data
    return {"error": f"Product {product_name} not found"}

@tool
def get_product_price(product_name: str):
    """Fetch the price and discount information of a product."""
    url = f"{BASE_URL}/search?q={product_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
    
        
        return data
    return {"error": f"Product {product_name} not found"}

@tool
def get_product_stock(product_name: str):
    """Check stock availability for a product."""
    url = f"{BASE_URL}/search?q={product_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data
    return {"error": f"Product {product_name} not found"}

@tool
def get_product_shipping_info(product_name: str):
    """Get shipping information for a product."""
    url = f"{BASE_URL}/search?q={product_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data
    return {"error": f"Product {product_name} not found"}

@tool
def get_product_warranty_info(product_name: str):
    """Get warranty information for a product."""
    url = f"{BASE_URL}/search?q={product_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data
    return {"error": f"Product {product_name} not found"}

# ========== FILTERING & COMPARISON TOOLS ==========

@tool
def get_products_price_less_than(max_price: float):
    """Get products priced below a given value."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        data= [p for p in products if p["price"] < max_price]

        filtered_products = []
        for product in data:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}

@tool
def get_products_price_greater_than(min_price: float):
    """Get products priced above a given value."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        data = [p for p in products if p["price"] > min_price]
        filtered_products = []
        for product in data:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}

@tool
def get_products_rating_less_than(rating: float):
    """Get products with rating below a given value."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        data = [p for p in products if p["rating"] < rating]
        filtered_products = []
        for product in data:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}

@tool
def get_products_rating_greater_than(rating: float):
    """Get products with rating above a given value."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        data = [p for p in products if p["rating"] > rating]
        filtered_products = []
        for product in data:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}

# ========== SORTING TOOLS ==========

@tool
def get_products_sorted_by_price(order: str = "asc"):
    """Sort products by price (asc/desc)."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        reverse = order.lower() == "desc"
        sorted_products = sorted(products, key=lambda x: x["price"], reverse=reverse)
        filtered_products = []
        for product in sorted_products:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to sort products"}

@tool
def get_products_sorted_by_rating(order: str = "desc"):
    """Sort products by rating (asc/desc)."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        reverse = order.lower() == "desc"
        sorted_products = sorted(products, key=lambda x: x["rating"], reverse=reverse)
        filtered_products = []
        for product in sorted_products:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to sort products"}

@tool
def get_top_rated_products(limit: int = 10):
    """Get top N highest-rated products."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        top = sorted(products, key=lambda x: x["rating"], reverse=True)[:limit]
        filtered_products = []
        for product in top:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}

@tool
def get_low_stock_products(threshold: int = 10):
    """Get products that are running low on stock."""
    url = f"{BASE_URL}"
    res = requests.get(url)
    if res.status_code == 200:
        products = res.json()["products"]
        low_stock = [p for p in products if p["stock"] < threshold]
        filtered_products = []
        for product in low_stock:
            filtered_product = {key: product[key] for key in fields_to_keep if key in product}
            filtered_products.append(filtered_product)
        return filtered_products
    return {"error": "Unable to fetch products"}







# Collect all tools into a single list variable
tools = [
    get_product_by_id,
    search_product,
    get_products_by_category,
    get_product_reviews,
    get_product_price,
    get_product_stock,
    get_product_shipping_info,
    get_product_warranty_info,
    get_products_price_less_than,
    get_products_price_greater_than,
    get_products_rating_less_than,
    get_products_rating_greater_than,
    get_products_sorted_by_price,
    get_products_sorted_by_rating,
    get_top_rated_products,
    get_low_stock_products
]

def get_tools():
    return tools





