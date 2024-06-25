from typing import Iterable
from django.db import models
from datetime import datetime
# Create your models here.
class Url(models.Model):
    url_link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    created_at =models.DateTimeField(auto_created=True,default=datetime.now)
    
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        self.check_limit()
      
        
    def check_limit(self):
        if Url.objects.count() > 99:
            Url.objects.order_by('created_at').first().delete()
        