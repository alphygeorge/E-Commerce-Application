from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# Product model with custom manager
class ProductManager(models.Manager):
    def available_products(self):
        return self.filter(inventory__quantity__gt=0)  # Filter products with positive inventory

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    SKU = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    objects = ProductManager()

    def __str__(self):
        return self.name
        

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def calculate_lifetime_value(self):
        return Order.objects.filter(customer=self).aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        tax_rate = get_country_tax_rate(self.customer.country)
        return self.total_amount * tax_rate / 100

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

# OrderItem model with post-save signal
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_time_of_order = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Check if there's sufficient inventory for the product
        inventory = Inventory.objects.get(product=self.product)
        if self.quantity > inventory.quantity:
            raise ValidationError(f"Insufficient inventory for {self.product.name}")
        super().save(*args, **kwargs)

@receiver(post_save, sender=OrderItem)
def update_inventory(sender, instance, **kwargs):
    inventory = Inventory.objects.get(product=instance.product)
    inventory.quantity -= instance.quantity
    inventory.save()

# Function to get tax rate based on country
def get_country_tax_rate(country):
    # Example tax rates
    tax_rates = {
        'USA': 7,
        'UK': 20,
        'India': 18,
    }
    return tax_rates.get(country, 10)  # Default tax rate is 10%

# Inventory model
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    last_restocked_date = models.DateField(auto_now=True)

    # Restock threshold
    restock_threshold = 10  # Set threshold for restock alerts

    def save(self, *args, **kwargs):
        # Trigger restock alert if quantity is below the threshold
        if self.quantity < self.restock_threshold:
            print(f"Restock Alert for Product: {self.product.name}")
            print(f"The stock for {self.product.name} (SKU: {self.product.SKU}) is below the restock threshold.")
            print(f"Current inventory: {self.quantity}. Please restock this product.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Inventory for {self.product.name} - {self.quantity} units"
  