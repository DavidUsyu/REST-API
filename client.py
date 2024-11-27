import requests

BASE_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    product = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=product)
    if response.status_code == 201:
        print("Product added successfully!")
    else:
        print(f"Failed to add product: {response.json()}")

def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        print("Products:")
        for product in products:
            print(product)
    else:
        print("Failed to retrieve products.")

if __name__ == "__main__":
    # Example usage
    add_product("Laptop", "High-performance laptop", 999.99)
    add_product("Phone", "Latest smartphone", 799.99)
    get_products()
