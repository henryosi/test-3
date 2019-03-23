from django.db import models
from django.urls import reverse
from django.db import models

# Create your models here.
class Wishitem (models.Model):
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse ('home', kwargs={'wishitem_id' : self.id}) 