from django.contrib import admin
from django.urls import path

from django.urls import path, include
from .views import index, detail, ressources_page


urlpatterns = [
    path('', index, name='index'),
    path('detail/<str:slug>/', detail, name='detail'),
    path('ressources/', ressources_page, name='ressources'),
    path('contact/', include('contact.urls')),
]