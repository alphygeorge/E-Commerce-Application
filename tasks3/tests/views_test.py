
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..models import Customer, Product, Order, OrderItem, Inventory, Category
from django.utils.timezone import now
from django.db.models import QuerySet 
from datetime import timedelta
from django.contrib.auth import get_user_model 



class CustomerViewSetTest(APITestCase):
    def setUp(self):
        # Create a superuser for authentication
        self.superuser = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.force_authenticate(user=self.superuser)

        # Create a customer for testing
        self.customer = Customer.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            country='USA'
        )

    def test_customer_list(self):
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return one customer

    def test_customer_retrieve(self):
        response = self.client.get(reverse('customer-detail', args=[self.customer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.customer.email)

class SalesAnalyticsViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create mock customer, products, and orders
        self.category = Category.objects.create(name="Test Category")
        self.customer = Customer.objects.create(name="Jane Doe", email="jane@example.com", country="USA")
        self.product = Product.objects.create(name="Product 1", description="Test Product", SKU="P001", price=100.00, category=self.category)
        self.inventory = Inventory.objects.create(product=self.product, quantity=100)
        self.order = Order.objects.create(customer=self.customer, total_amount=200)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price_at_time_of_order=100.00)

    def test_revenue_by_category(self):
        url = reverse('revenue-by-category')
        response = self.client.get(url, {'start_date': '2024-01-01', 'end_date': '2024-12-31'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_revenue', response.data[0])

    def test_top_selling_products(self):
        url = reverse('top-selling-products')
        response = self.client.get(url, {'start_date': '2024-01-01', 'end_date': '2024-12-31', 'country': 'USA'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list) or isinstance(response.data, QuerySet))


class InventoryViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Test Category")

        # Create mock product and inventory
        self.product = Product.objects.create(name="Test Product", description="Test Description", SKU="SKU001", price=10.00, category=self.category)
        self.inventory = Inventory.objects.create(product=self.product, quantity=20)

    def test_inventory_update(self):
        url = reverse('inventory-update', args=[self.inventory.id])
        data = {'quantity': 30}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 30)



# class SalesViewSetTest(APITestCase):
#     def setUp(self):
#         # Create a superuser for authentication
#         self.superuser = get_user_model().objects.create_superuser(
#             username='admin', email='admin@example.com', password='password'
#         )
#         self.client.force_authenticate(user=self.superuser)

#         # Create a customer and an order for testing
#         self.customer = Customer.objects.create(
#             name='John Doe',
#             email='john.doe@example.com',
#             country='USA'
#         )
#         self.order = Order.objects.create(
#             customer=self.customer,
#             total_amount=100.00
#         )
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             product=Product.objects.create(name='Product A', description='Sample Product', SKU='SKU001', price=10.00, category=Category.objects.create(name='Category A')),
#             quantity=2,
#             price_at_time_of_order=10.00
#         )

#     def test_export_monthly_sales(self):
#         current_year = 2024
#         current_month = 10
#         url = reverse('export-monthly-sales', args=[current_year, current_month])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response['Content-Disposition'], f'attachment; filename="monthly_sales_report_{current_year}_{current_month}.xlsx"')

class SalesViewSetTest(APITestCase):
    def setUp(self):
        # Create a superuser for authentication
        self.superuser = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.force_authenticate(user=self.superuser)

        # Create a customer and a product for testing
        self.customer = Customer.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            country='USA'
        )
        
        # Create a category and product
        self.category = Category.objects.create(name='Category A')
        self.product = Product.objects.create(
            name='Product A',
            description='Sample Product',
            SKU='SKU001',
            price=10.00,
            category=self.category
        )
        
        # Create inventory for the product
        self.inventory = Inventory.objects.create(
            product=self.product,
            quantity=100  # Set initial quantity
        )

        # Create an order and order item
        self.order = Order.objects.create(
            customer=self.customer,
            total_amount=20.00  # Example total amount
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price_at_time_of_order=self.product.price  # Price per item
        )

    def test_export_monthly_sales(self):
        current_year = 2024
        current_month = 10
        url = reverse('export_monthly_sales', args=[current_year, current_month])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="monthly_sales_report_{current_year}_{current_month}.xlsx"'
        )
