from django.conf import settings
from django.db import models
from django.urls import reverse

STATUS= (('active','active'),('','default'))
STOCK=(('In-stock','In-stock'),('Out-of-stock','Out-of-stock'))
Labels=(('Hot','Hot'),('Sale','Sale'),('New','New'))

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)
    status=models.CharField(max_length=100, choices=STATUS,blank=True)

    def __str__(self):
        return self.title

    def get_category_url(self):
        return reverse("home:category",kwargs={'slug' : self.slug})


class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=100, choices=STATUS, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_subcategory_url(self):
        return reverse("home:subcategory",kwargs={'slug':self.slug})

class Item(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    discounted_price=models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    slug=models.CharField(max_length=300,unique=True)
    labels=models.CharField(choices=Labels, max_length=100, blank=True)
    brand=models.CharField(max_length=200)
    special_offer=models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    stock=models.CharField(max_length=200,choices=STOCK)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title

    def specials_offers(self):
        return self.price - self.discounted_price

    def get_item_url(self):
        return reverse("home:product",kwargs={'slug' : self.slug})

    def add_to_cart(self):
        return reverse("home:add_to_cart",kwargs={'slug' : self.slug})

class Slider(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    rank=models.IntegerField()
    status=models.CharField(choices = STATUS, max_length=100, blank = True)
    upper_part=models.CharField(max_length=300)
    lower_part=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    status=models.CharField(choices = STATUS, max_length=100, blank = True)
    upper_part=models.CharField(max_length=300)
    middle_part = models.CharField(max_length=300)
    lower_part=models.CharField(max_length=200, blank=True)
    cross_part = models.CharField(max_length=300, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.TextField()
    title = models.CharField(max_length=100,blank=True)
    image = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete_cart(self):
        return reverse("home:delete_cart",kwargs={'slug' : self.slug})

