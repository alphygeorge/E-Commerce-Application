from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum, Count
from .models import Order, Product, Category, Customer

class SalesAnalytics:
    @staticmethod
    def calculate_revenue_by_category(start_date, end_date):
        """
        Calculate revenue for each product category over a specified time period.
        """
        return (
            Order.objects.filter(order_date__range=[start_date, end_date])
            .values('orderitem__product__category__name')
            .annotate(total_revenue=Sum('orderitem__price_at_time_of_order'))
            .order_by('-total_revenue')
        )

    @staticmethod
    def top_selling_products_by_country(start_date, end_date, country):
        """
        Identify the top-selling products by country over a specified time period.
        """
        return (
            Order.objects.filter(customer__country=country, order_date__range=[start_date, end_date])
            .values('orderitem__product__name')
            .annotate(total_sold=Sum('orderitem__quantity'))
            .order_by('-total_sold')
        )

    @staticmethod
    def calculate_churn_rate():
        """
        Compute customer churn rate (customers who haven't placed an order in the last 6 months).
        """
        six_months_ago = timezone.now() - timedelta(days=180)
        total_customers = Customer.objects.count()
        inactive_customers = Customer.objects.filter(order__order_date__lt=six_months_ago).distinct().count()

        if total_customers == 0:
            return 0
        return (inactive_customers / total_customers) * 100






