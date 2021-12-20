from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=18)
    phone=models.CharField(max_length=12)
    name=models.CharField(max_length=12)
    address=models.TextField()
    date=models.DateField()
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class signup(models.Model):
    username=models.CharField(max_length=18)
    email=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
def __str__(self):
                           # for database as all new data save with name....
    return self.username

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")

def __str__(self):
    return self.product_name
          
   
    

    
