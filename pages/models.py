from django.db import models
from django.urls import reverse

# Create your models here.
class BookNow(models.Model):

    DestinationPicture = models.ImageField(upload_to='picture/', blank=True) # have used pillow for this
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class CustomerProfile(models.Model):
    full_name= models.CharField(max_length= 100,blank= True)
    place_you_want_to_visit= models.CharField(max_length=100,blank= True)
    age= models.CharField(max_length= 100,blank= True)
    gender= models.CharField(max_length= 100,blank= True)
    contact_no =models.CharField( max_length=10,blank =True)
    email_add= models.CharField(max_length= 100,blank= True)
    address = models.CharField(max_length= 300,blank= True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('thankyou')

 
