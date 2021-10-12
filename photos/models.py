from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.category_name

    @classmethod
    def search_by_name(cls,search_term):
        category_name = cls.objects.filter(photos=search_term)
        return category_name


class Photos(models.Model):
    category = models.ForeignKey(Category,on_delete=SET_NULL,null=True)
    image = CloudinaryField('image')
    # image = ImageField(null=False,blank=False)
    image_name = models.CharField(max_length=100,null=False,blank=False,default='Name_of_image')
    description = models.TextField()
    image_location = models.CharField(max_length=50,null=False,blank=False,default='Location_image_was_taken')

    def __str__(self):
        return self.image_name
    

