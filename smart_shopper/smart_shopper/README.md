The Smart Shopper's Dilemma: Real-time Product API
This project is a Django-based web API designed to solve the "Smart Shopper's Dilemma." It provides a real-time, high-speed product information pipeline optimized for fetching product details quickly and efficiently. The API uses asynchronous programming to handle concurrent requests, ensuring a fast and responsive user experience.

Features
Real-time Data: Fetches up-to-date product information on demand.

Optimized Performance: Uses asynchronous requests to minimize latency and handle multiple product searches efficiently.

Scalable Architecture: Built on Django and Django REST Framework, providing a robust and scalable foundation.

Clean API Interface: A simple and intuitive REST endpoint for clients to query product information.

Prerequisites
Python 3.9 or higher

pip (Python package installer)

Setup and Running the Project
Follow these steps to set up and run the project in your VS Code environment.

Open a Terminal in VS Code:
In VS Code, open a new terminal by navigating to Terminal > New Terminal. This will open the terminal in the root directory of your project.

Create a Virtual Environment:
It's a best practice to use a virtual environment to manage project dependencies.

python -m venv venv

Activate the Virtual Environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate

Install Required Packages:
The requirements.txt file lists all the necessary Python libraries.

pip install -r requirements.txt

Run the Django Development Server:
Navigate into the main project directory and run the server.

cd smart_shopper
python manage.py runserver

The server will start, and you will see a message like:
Starting development server at http://127.0.0.1:8000/

API Usage
The API has a single endpoint for searching products.

Endpoint: /api/v1/search/
Method: GET

Parameters:

product (string, required): The name of the product you want to search for.

Example API Calls
You can test the API by navigating to these URLs in your web browser.

Example 1: Searching for "365 WholeFoods Peanut Butter"

URL: http://127.0.0.1:8000/api/v1/search/?product=365+WholeFoods+Peanut+Butter

Example 2: Searching for "Google Pixel 8"

URL: http://127.0.0.1:8000/api/v1/search/?product=Google+Pixel+8

Note: The system uses a simulated search and data extraction process to demonstrate the pipeline's core functionality. In a real-world scenario, you would integrate with a robust scraping or e-commerce API service.