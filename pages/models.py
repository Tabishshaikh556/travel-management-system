from django.db import models

# Create your models here.
class BookNow(models.Model):

    DestinationPicture = models.ImageField(upload_to='picture/', blank=True) # have used pillow for this
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
