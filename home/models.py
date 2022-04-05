from django.db import models

# Create your models here.

class Nav (models.Model):
    nav_title = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)


class Footer (models.Model):
    bio = models.TextField(help_text='enter your bio or about us information here')
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    subscribe = models.EmailField(max_length=254)