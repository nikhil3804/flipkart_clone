from django.db import models
class d1(models.Model):
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
   # image=models.ImageField(max_length=122)
   # mobile=models.CharField(max_length=122)


class d2(models.Model):
    Address=models.CharField(max_length=122)
    Street_name=models.CharField(max_length=122)
    Near_location=models.CharField(max_length=122)
   # image=models.ImageField(max_length=122)
    
    




#class d3(models.Model):

    #Address=models.CharField(max_length=122)
   # Street_name=models.CharField(max_length=122)
   # Near_location=models.CharField(max_length=122)
   # ImageField=models.ImageField(upload_to="c1/c2")



    
   

# Create your models here.
