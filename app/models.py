from django.db import models
from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     image = models.ImageField(upload_to='category',null=True,blank=True)
#     description = models.TextField(null=True, blank=True)
#     def __str__(self):
#         return self.name
class Product(models.Model):
    status = {
        ('NONE', 'NONE'),
        ('dessert', 'dessert'),
        ('drink', 'drink'),
        ('meal', 'meal')
    }
    name = models.CharField(max_length=100, null=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    status = models.CharField(max_length=50, default='NONE',choices=status)
    description = models.TextField(null=True)
    def __str__(self):
        return f'''{self.name}'''

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Team(models.Model):
    fname = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='team',null=True,default='team/chef.png')
    description = models.TextField(null=True)
    s_facebook = models.CharField(max_length=100,null=True,blank=True)
    s_twitter = models.CharField(max_length=100,null=True,blank=True)
    s_in = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.fname
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
