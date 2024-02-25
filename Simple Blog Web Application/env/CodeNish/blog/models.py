from django.db import models
import uuid

class blogTable(models.Model):
    name =models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(default='Screenshot (3).png',null=True,blank=True)
    image1 = models.ImageField(default='Screenshot (3).png',null=True,blank=True)
    image2 = models.ImageField(default='Screenshot (3).png',null=True,blank=True)
    id =models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def __str__(self):
        return self.name