# recommendation_engine.py

import random
from .models import Order, OrderItem, Customer  # Ensure these imports are correct

class RecommendationEngine:
    @staticmethod
    def recommend_products(customer):
        # Get the customer's order history
        orders = Order.objects.filter(customer=customer)
        purchased_products = set()

        for order in orders:
            order_items = OrderItem.objects.filter(order=order)
            for item in order_items:
                purchased_products.add(item.product)

        # Get similar customers' purchases
        similar_customers = Customer.objects.exclude(id=customer.id).filter(country=customer.country)
        similar_purchased_products = set()

        for similar_customer in similar_customers:
            similar_orders = Order.objects.filter(customer=similar_customer)
            for similar_order in similar_orders:
                similar_order_items = OrderItem.objects.filter(order=similar_order)
                for similar_item in similar_order_items:
                    similar_purchased_products.add(similar_item.product)

        # Combine purchased products and similar purchases
        recommendations = (purchased_products.union(similar_purchased_products))

        # Exclude already purchased products from recommendations
        recommendations = recommendations.difference(purchased_products)

        # Filter by current inventory levels
        available_recommendations = [product for product in recommendations if product.inventory.quantity > 0]

        # Randomly select a few products to recommend
        return random.sample(available_recommendations, min(5, len(available_recommendations)))  # Recommend up to 5 products
