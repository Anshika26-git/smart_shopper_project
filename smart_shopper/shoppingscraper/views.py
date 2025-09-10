import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class ProductSearchView(APIView):
    """
    API view for searching product information.
    Leverages asyncio for efficient, non-blocking requests.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to search for a product.
        The product name is provided as a query parameter.
        """
        product_name = request.query_params.get('product')

        if not product_name:
            return Response(
                {"error": "Product name is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Run the asynchronous function to fetch product data
        try:
            results = asyncio.run(self._fetch_and_process_product_data(product_name))
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    async def _fetch_and_process_product_data(self, product_name):
        """
        Simulates fetching and processing product data from multiple sources concurrently.
        """
        # Simulate fetching different pieces of information in parallel
        tasks = [
            self._fetch_brand(product_name),
            self._fetch_price(product_name),
            self._fetch_weight(product_name),
        ]

        # Use asyncio.gather() to run all tasks concurrently
        brand, price, weight = await asyncio.gather(*tasks)

        # Combine the results into a single structured product card
        product_card = {
            "product_name": product_name,
            "brand": brand,
            "price": price,
            "total_weight": weight,
        }

        return {
            "query": product_name,
            "product_card": product_card,
        }

    async def _fetch_brand(self, product_name):
        """
        Simulates fetching the brand from a remote source.
        """
        # Simulate a network request with a delay
        await asyncio.sleep(1) 

        # This is a hard-coded simulation for demonstration purposes
        if "peanut butter" in product_name.lower():
            return "365 WholeFoods Market"
        if "pixel" in product_name.lower():
            return "Google"
        return "Unknown Brand"

    async def _fetch_price(self, product_name):
        """
        Simulates fetching the price from a remote source.
        """
        # Simulate a network request with a delay
        await asyncio.sleep(1.5) 

        # Hard-coded simulation
        if "peanut butter" in product_name.lower():
            return "$5.99"
        if "pixel" in product_name.lower():
            return "$699.00"
        return "Price Unavailable"

    async def _fetch_weight(self, product_name):
        """
        Simulates fetching the total weight from a remote source.
        """
        # Simulate a network request with a delay
        await asyncio.sleep(0.5) 

        # Hard-coded simulation
        if "peanut butter" in product_name.lower():
            return "16 oz"
        if "pixel" in product_name.lower():
            return "187 g"
        return "Weight Unavailable"