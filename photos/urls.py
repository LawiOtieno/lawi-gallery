from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path('',views.gallery,name = 'gallery'),
    path('photos/<str:pk>/',views.viewPhotos,name = 'photos'),
    path('add-photos/', views.addPhotos, name='add-photos'),
    path('search', views.search_results,name ='search_results'),
]