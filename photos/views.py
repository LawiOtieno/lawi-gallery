from django.shortcuts import redirect, render

# import photos
from .models import Category,Photos

# import photos

# Create your views here.

def gallery(request):
    category=request.GET.get('category')
    if category==None:
        photos=Photos.objects.all()
    else:
        photos=Photos.objects.filter(category__category_name=category)


    categories = Category.objects.all()

    context = {'categories':categories, 'photos':photos}
    return render(request, 'all-photos/gallery.html',context)

def viewPhotos(request, pk): # pk
    photo = Photos.objects.get(id=pk)

    return render(request, 'all-photos/photos.html',{'photo':photo})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any Category"
        return render(request, 'all-photos/search.html',{"message":message})


def addPhotos(request):
    categories = Category.objects.all()

    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category,created=Category.objects.get_or_create(category_name=data['new_category'])
        else:
            category=None


        photo = Photos.objects.create(
            category=category,
            image_name=data['image_name'],
            description=data['description'],
            image_location=data['image_location'],
            image=image,
        )
        return redirect


    context = {'categories':categories}
    return render(request, 'all-photos/add-photos.html',context)

