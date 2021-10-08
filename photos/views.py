from django.shortcuts import render
from .models import Category,Photos

import photos

# Create your views here.

def gallery(request):
    categories = Category.objects.all()

    
    context = {'categories':categories}
    return render(request, 'all-photos/gallery.html',context)

def viewPhotos(request, pk): # pk
    return render(request, 'all-photos/photos.html')

def addPhotos(request):
    return render(request, 'all-photos/add-photos.html')

