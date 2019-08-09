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
    customer_name = models.CharField(max_length = 100)
    customer_phone = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    select_product = models.TextField(max_length = 200)
    tot_price = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name

    def secretphone(self):
        return self.customer_phone[-4:]