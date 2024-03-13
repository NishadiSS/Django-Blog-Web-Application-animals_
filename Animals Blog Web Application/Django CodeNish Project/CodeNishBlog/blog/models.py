from django.db import models
import uuid

class blogTable(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    image1=models.ImageField(default='default.jpg',null=True,blank=True)
    image2=models.ImageField(default='default.jpg',null=True,blank=True)
    image3=models.ImageField(default='default.jpg',null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def __str__(self):
        return self.name

    
# Create your models here.
