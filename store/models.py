from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()  # A TextField is usually used for descriptions
    # image = models.ImageField(upload_to='uploads/products/')  # 'upload_to' specifies where images will be stored
    image = models.ImageField(upload_to='uploads/products/') 
    def __str__(self):
        return self.name





class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
