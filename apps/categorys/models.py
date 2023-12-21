from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            max_size = (300, 300)
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size)
                img.save(self.image.path)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            max_size = (300, 300)
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size)
                img.save(self.image.path)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def calculate_total_price(self):
        total_price = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def save(self, *args, **kwargs):
        super(CartItem, self).save(*args, **kwargs)
        self.cart.calculate_total_price()

    def delete(self, *args, **kwargs):
        super(CartItem, self).delete(*args, **kwargs)
        self.cart.calculate_total_price()

