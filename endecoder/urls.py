
from .views import *
from django.urls import path,include

urlpatterns = [
    path('', index_render , name='index'),
]
