from django.shortcuts import render
from .models import Category,Photos

# import photos

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photos.objects.all()

    context = {'categories':categories, 'photos':photos}
    return render(request, 'all-photos/gallery.html',context)

def viewPhotos(request, pk): # pk
    photo = Photos.objects.get(id=pk)

    return render(request, 'all-photos/photos.html',{'photo':photo})

def addPhotos(request):
    return render(request, 'all-photos/add-photos.html')

