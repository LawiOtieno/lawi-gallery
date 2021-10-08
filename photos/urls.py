from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.gallery,name = 'gallery'),
    url(r'^photos/<str:pk>/',views.viewPhotos,name = 'photos'),
    url(r'^add-photos/', views.addPhotos, name='add-photos'),
    # url(r'',,name =''),
]