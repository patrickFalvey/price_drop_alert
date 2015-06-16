from django.db import models



class Price_Drop_Alert(models.Model):
    email = models.EmailField()
    item = models.CharField(max_length=150,default=None)
    price = models.FloatField()


   


