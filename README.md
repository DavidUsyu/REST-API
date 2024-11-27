# REST API for Product Management

## Overview
This is a simple REST API built using Flask to manage products with the following fields:
- `name` (string): Product name
- `description` (string): Product description
- `price` (float): Product price

## Endpoints
### POST /products
- **Description**: Creates a new product.
- **Request Body**:
  ```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 99.99
  }
  ````
  Response:
  
    201 Created: Product created successfully.
  
    400 Bad Request: Invalid input.
  
  GET /products
    Description: Retrieves a list of all products.
    Response: 200
  
    OK: List of products.

  SETUP INSTRUCTIONS:

  PREREQUISITES:

    Python 3.x

  pip (Python package manager)

  Installation:

    Clone this repository or copy the project files.
    Install Flask:
  ```bash
  pip install Flask
  ````
  Running the API Server
  ```bash
  python app.py
  ````
  Testing the API
  ```bash
  python client.py
  ````
  Example Requests:
  
  Add a Product:
  ```bash
  curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "TV", "description": "Smart TV", "price": 499.99}'
  ````
  Get All Products:
  ```bash
  curl http://127.0.0.1:5000/products
  ````
