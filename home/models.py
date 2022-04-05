from django.db import models

# Create your models here.

class Footer (models.Model):
    bio = models.TextField(help_text='enter your bio or about us information here')
    subscribe = models.EmailField(max_length=254)


class SocialMedia (models.Model):
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)