from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from .models import Customer, Order,OrderItem, Inventory, Product
from django.http import HttpResponse
from openpyxl import Workbook
from datetime import datetime
from rest_framework.permissions import AllowAny
from .sales_analytics import SalesAnalytics
from django.db.models import Sum
from .serializers import CustomerSerializer, ProductSerializer , InventoryUpdateSerializer
from .recommendation_engine import RecommendationEngine  


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            customer = self.get_object()
        except Customer.DoesNotExist:
            raise NotFound("Customer not found.")
        
        serializer = self.get_serializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        try:
            customers = self.queryset
            serializer = self.get_serializer(customers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  

    def list_available_products(self, request):
        available_products = Product.objects.available_products()  
        serializer = ProductSerializer(available_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """ List all products (optional, if you want to allow listing all products) """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SalesViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]  

    def export_monthly_sales(self, request, year, month):
        # Validate the month
        if month < 1 or month > 12:
            return Response({"error": "Month must be between 1 and 12."}, status=status.HTTP_400_BAD_REQUEST)

        # Filter orders by the specified year and month
        orders = Order.objects.filter(order_date__year=year, order_date__month=month)

        # Create a workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Monthly Sales Report"

        # Add headers to the worksheet
        

        worksheet.append([
            "Order ID", 
            "Customer", 
            "Order Date", 
            "Product Name", 
            "Quantity", 
            
            "Total Revenue"
        ])

        # Populate the worksheet with order data
        for order in orders:
            order_items = OrderItem.objects.filter(order=order)
            for item in order_items:
                total_revenue = item.quantity * item.price_at_time_of_order
                worksheet.append([
                    order.id, 
                    order.customer.name, 
                    order.order_date, 
                    item.product.name, 
                    item.quantity, 
                    
                    total_revenue
                ])
        # Create a response object
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="monthly_sales_report_{year}_{month}.xlsx"'

        # Save the workbook to the response
        workbook.save(response)

        return response





class SalesAnalyticsViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  
    def revenue_by_category(self, request):
        try:
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')

            if not start_date or not end_date:
                return Response({"error": "Both start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            revenue = SalesAnalytics.calculate_revenue_by_category(start_date, end_date)
            return Response(revenue, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def top_selling_products(self, request):
        try:
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            country = request.query_params.get('country')

            if not start_date or not end_date or not country:
                return Response({"error": "start_date, end_date, and country are required."}, status=status.HTTP_400_BAD_REQUEST)

            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            top_products = SalesAnalytics.top_selling_products_by_country(start_date, end_date, country)
            return Response(top_products, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def churn_rate(self, request):
        try:
            churn_rate = SalesAnalytics.calculate_churn_rate()
            return Response({"churn_rate": churn_rate}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    
    def aggregated_salesdata(self, request):
        # Calculate total sales revenue
        total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

        # Calculate total number of orders
        total_orders = Order.objects.count()

        # Prepare response data
        aggregated_data = {
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            
        }

        return Response(aggregated_data)



class RecommendationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  
    def list(self, request):
        customer_id = request.query_params.get('customer_id')

        if not customer_id:
            return Response({"error": "customer_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(id=customer_id)
            recommended_products = RecommendationEngine.recommend_products(customer)
            serializer = ProductSerializer(recommended_products, many=True)  # Assuming you have a ProductSerializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class InventoryViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  

    def update(self, request, pk=None):
        try:
           inventory = Inventory.objects.get(product_id=pk)
        except inventory.DoesNotExist:
            return Response({"error": "Inventory not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryUpdateSerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        