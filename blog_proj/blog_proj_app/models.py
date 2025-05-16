from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=40)
    email= models.CharField(max_length=16)
    content= models.CharField(max_length=100)
    number= models.IntegerField(max_length=10)

    def __self__(self):
        return(self.name)