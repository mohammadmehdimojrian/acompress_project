
from .views import *
from django.urls import path

urlpatterns = [
    path('', index_render , name='index'),
    path('output/', output_render , name='output'),
]
