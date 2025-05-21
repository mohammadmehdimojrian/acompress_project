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
        encoded_huffman,codebook= huffman_encode(text)
        encoded_huffman_size = ceil(len(encoded_huffman)/8)
        encoded_rle = RLE_encode(text)
        encoded_rle_size = len(encoded_rle)
        
        context={"original_text" : text , 
                 "original_text_size" : len(text) ,
                 "encoded_huffman" : encoded_huffman , 
                 "encoded_rle" : encoded_rle , 
                 "encoded_huffman_size" :encoded_huffman_size ,
                 "encoded_rle_size" : encoded_rle_size ,
                 "codebook": codebook ,
                 
                 }
    return render(request , 'output.html' , context)

def decompress_rle_render(request , rle_compressed:str):
    # print(rle_compressed)
    decompressed_string = RLE_decode(rle_compressed)
    context = {'rle_compressed' : rle_compressed , 'decompressed_string': decompressed_string }
    return render(request , 'decompress_rle.html',context)

def decompress_huffman_render(request ,huffman_compressed:str , original_string:str ):
    # print(original_string)
    codebook = huffman_encode(original_string)[1]
    decompressed = huffman_decode(encoded=huffman_compressed , codebook=codebook)
    # print(decompressed)
    context={ 'decompressed' :decompressed , 'huffman_compressed' : huffman_compressed} 
    return render(request,'decompress_huffman.html',context)
    
    
# Create your views here.
