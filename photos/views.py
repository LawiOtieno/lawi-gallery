from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'all-photos/gallery.html')

def viewPhotos(request, pk):
    return render(request, 'all-photos/photos.html')

def addPhotos(request):
    return render(request, 'all-photos/add-photos.html')
