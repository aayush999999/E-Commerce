from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateField()

    def __str__(self):
        return self.name
    



class ItemInsert(models.Model): 
    item_group = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=30)
    stock_qty = models.IntegerField(max_length=30)
    item_rate = models.IntegerField(max_length=30, default="")
    item_date = models.DateField()
    image = models.ImageField(upload_to="seller/images", default="")

    def __str__(self):
        return self.item_desc
    



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    mobile = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name    
      

class Checkout(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=1000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    addr = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    number = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        ItemInsert,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    quantity = models.IntegerField(default=0, blank=True, null=True)
    
