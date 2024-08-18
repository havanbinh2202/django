from django.db import models

from django.contrib.auth.models import User
# Create your models here.
# loại sản phẩm
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) #tạo một slug duy nhất cho mỗi danh mục
    description = models.TextField(max_length=100,default='') #mô tả

    def __str__(self):
        return self.name
    
# sản phẩm
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    @property
    def Imgurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# giỏ hàng  
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username}'s Cart: {self.product.name}"

    @staticmethod
    def total_quantity(user):
        # Tính tổng số sản phẩm trong giỏ hàng của một người dùng cụ thể
        cart_items = CartItem.objects.filter(user=user)
        total_quantity = sum(item.quantity for item in cart_items)
        return total_quantity
    
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    mobile = models.IntegerField(null=True, blank=True)
    add_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.address