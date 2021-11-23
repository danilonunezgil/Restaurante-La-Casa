from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import DecimalField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
from djmoney.models.fields import MoneyField

User = get_user_model()
"""""
Definition of ecommerce models
"""
class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150, help_text="Register an address ")
    address_line_2 = models.CharField(max_length=150, help_text="Register a second address")
    city = models.CharField(max_length=100, help_text="City where the purchase is made")
    zip_code = models.CharField(max_length=100, help_text="City zip code")
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, help_text="Allows you to choose between different types of addresses")
    default = models.BooleanField(default=False, help_text="Allows to set default address")
    
    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.zip_code} "

    class Meta:
        verbose_name_plural = 'Addresses'


class Product(models.Model):
    """
    class to store a product.
    """
    title = models.CharField(max_length=150, help_text="Name of product, example product 1")
    slug = models.SlugField(unique=True, help_text="A short name, generally used in URLs.")
    image = models.ImageField(upload_to='product_images')
    descritption = models.TextField(help_text="Here you must write the product description")
    price = MoneyField(
        default = 0,
        decimal_places = 2,
        default_currency='USD',
        max_digits = 11,
        help_text="Price of product")
    stock = models.IntegerField(default=0, help_text="Stock of product")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False, help_text="Field to know if the product is active or not active")
    
    def __str__(self):
        """Return title of product."""
        return self.title

    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={'slug': self.slug})
    
    @property
    def in_stock(self):
        return self.stock > 0


class OrderItem(models.Model):
    """
    This model is the relation between the producto and the order.
    """
    order = models.ForeignKey("Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, help_text="Quantity you want to buy")
    
    def __str__(self):
        """ Return quantity and title of product"""
        return f"{self.quantity} x {self.product.title}"
    
class Order(models.Model):
    """
    This class allows you to purchase a product, related to, model: `auth.User`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Name of the user making the purchase ")
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True, help_text="Date of purchase")
    ordered = models.BooleanField(default=False)

    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Return reference number of the order"""
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"
    
class Payment(models.Model):
    """
    This class allows you to make a payment for an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('Paypal', 'Paypal'),
        ),help_text="Select payment method")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Date of payment")
    succesful = models.BooleanField(default=False, help_text="Successful payment?")
    amount = models.FloatField(help_text="Amount paid")
    raw_response = models.TextField(help_text="Payment gateway response")

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender=Product)