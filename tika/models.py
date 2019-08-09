from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Order(models.Model):
    customer_name = models.CharField(max_length = 10)
    customer_phone = models.CharField(max_length = 11)
    location = models.CharField(max_length = 2)
    select_product = models.CharField()
    total_price = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.customer_name

    def secretphone(self):
        return self.customer_phone[-4:]