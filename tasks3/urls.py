from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, SalesViewSet, SalesAnalyticsViewSet, RecommendationViewSet, InventoryViewSet, ProductViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)  # Register CustomerViewSet
router.register(r'sales', SalesViewSet, basename='sales')  # Register SalesViewSet for exporting sales reports
router.register(r'recommendations', RecommendationViewSet, basename='recommendations')  # Register RecommendationViewSet
router.register(r'inventory', InventoryViewSet, basename='inventory') 
router.register(r'products', ProductViewSet, basename='products')  # Register ProductViewSet

sales_analytics = SalesAnalyticsViewSet.as_view({
    'get': 'revenue_by_category'
})

top_selling_products = SalesAnalyticsViewSet.as_view({
    'get': 'top_selling_products'
})

churn_rate = SalesAnalyticsViewSet.as_view({
    'get': 'churn_rate'
})

aggregated_salesdata= SalesAnalyticsViewSet.as_view({
    'get': 'aggregated_salesdata'
})


urlpatterns = [
    path('', include(router.urls)),  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain access & refresh tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint to refresh the access token
    path('sales/export/<int:year>/<int:month>/', SalesViewSet.as_view({'get': 'export_monthly_sales'}), name='export_monthly_sales'),
    path('analytics/revenue-by-category/', sales_analytics, name='revenue-by-category'),
    path('analytics/top-selling-products/', top_selling_products, name='top-selling-products'),
    path('analytics/churn-rate/', churn_rate, name='churn-rate'),
    path('analytics/aggregated-salesdata/', aggregated_salesdata, name= 'aggregated_salesdata'),
    path('inventory/<int:pk>/update/', InventoryViewSet.as_view({'put': 'update'}), name='inventory-update'),
    path('products/available/', ProductViewSet.as_view({'get': 'list_available_products'}), name='available-products'),
]
