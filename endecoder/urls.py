
from .views import *
from django.urls import path

urlpatterns = [
    path('', index_render , name='index'),
    path('output/', output_render , name='output'),
    path('decompress_rle/<str:rle_compressed>/', decompress_rle_render , name='rle_decompress'),
    path('decompress_huffman/<str:huffman_compressed>/<str:original_string>/', decompress_huffman_render , name='huffman_decompress'),
]
