import requests

from app.types import TProduct

FAKE_STORE_API_URL = "https://fakestoreapi.com"


def fetch_product(product_id):
    try:
        response = requests.get(f"{FAKE_STORE_API_URL}/products/{product_id}")
        response_data = response.json()

        product = {
            "id": response_data.get("id"),
            "title": response_data.get("title"),
            "image": response_data.get("image"),
            "price": response_data.get("price"),
            "review": str(response_data.get("rating").get("rate"))
        }

        return TProduct(**product)
    except Exception as error:
        print("Erro ao buscar produtos", error)
        return None
