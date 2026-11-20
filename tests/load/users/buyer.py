
import random

from locust import HttpUser, task, between

from tests.load.common.config import API_PREFIX


class BuyerUser(HttpUser):

    wait_time = between(2, 5)

    @task
    def browse_shops(self):

        shops_response = self.client.get(
            f"{API_PREFIX}/shops",
            name="/shops"
        )

        if shops_response.status_code != 200:
            return

        shops = shops_response.json()

        if not shops:
            return

        shop = random.choice(shops)
        shop_id = shop["id"]

        self.client.get(
            f"{API_PREFIX}/shops/{shop_id}",
            name="/shops/[shop_id]"
        )

        products_response = self.client.get(
            f"{API_PREFIX}/shops/{shop_id}/products",
            name="/shops/[shop_id]/products"
        )

        if products_response.status_code != 200:
            return

        products = products_response.json()

        if not products:
            return

        product = random.choice(products)
        product_id = product["id"]

        self.client.get(
            f"{API_PREFIX}/products/{product_id}",
            name="/products/[product_id]"
        )
