from django.shortcuts import render , redirect
from rle import *
from huffman import *
from math import ceil
def index_render(request):
    if request.method =='POST':
        text = request.POST['text']
        rle_encoded = RLE_encode(text)
        huffman_encoded = huffman_encode(text)[0]
        context={'rle_encoded' : rle_encoded , 'huffman_encoded' : huffman_encoded}
        # request.session['text'] = text
        # request.session['original_text'] = {'text': text}
        # return HttpResponseRedirect(redirect_to='output' , kwargs={'text':text})
        # return redirect('output')
    
        # print(rle_encoded)
        # print(huffman_encoded)
    return render(request , 'index.html')

def output_render(request):
    if request.method=="POST":
        text = request.POST.get('text')
        encoded_huffman = huffman_encode(text)[0]
        encoded_huffman_size = ceil(len(encoded_huffman)/8)
        encoded_rle = RLE_encode(text)
        encoded_rle_size = len(encoded_rle)
        
        context={"original_text" : text , 
                 "original_text_size" : len(text) ,
                 "encoded_huffman" : encoded_huffman , 
                 "encoded_rle" : encoded_rle , 
                 "encoded_huffman_size" :encoded_huffman_size ,
                 "encoded_rle_size" : encoded_rle_size
                 
                 }
    return render(request , 'output.html' , context)
# Create your views here.
