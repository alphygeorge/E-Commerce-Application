
import random
from .models import OrderItem, Customer  # Ensure these imports are correct

class RecommendationEngine:
    @staticmethod
    def recommend_products(customer):
        # Get the customer's purchased products
        purchased_products = set(OrderItem.objects.filter(order__customer=customer).values_list('product', flat=True))

        # Get similar customers' purchases, excluding the current customer's purchases
        similar_customers = Customer.objects.filter(country=customer.country).exclude(id=customer.id)
        similar_purchased_products = set(OrderItem.objects.filter(order__customer__in=similar_customers).values_list('product', flat=True))

        # Combine similar and purchased products, then remove already purchased products
        recommendations = similar_purchased_products.difference(purchased_products)

        # Filter recommendations by available inventory
        available_recommendations = [product for product in recommendations if product.inventory.quantity > 0]

        # Return up to 5 random product recommendations
        return random.sample(available_recommendations, min(5, len(available_recommendations)))
