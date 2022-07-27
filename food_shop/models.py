from django.db import models
from django.contrib.auth.models import User



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d")
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # facebook_url = models.URLField(default="")
    # twitter_url = models.URLField(default="")

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="dishes/%Y/%m/%d")
    ingredients = models.TextField()
    details = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    disccounted_price = models.FloatField(blank=True)
    is_available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural = "Dish Table"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profiles/%Y/%m/%d", null=True, blank=True)
    address = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = "Profile Table"    
    