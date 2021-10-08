from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.category_name

class Photos(models.Model):
    category = models.ForeignKey(Category,on_delete=SET_NULL,null=True)
    image = ImageField(null=False,blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
