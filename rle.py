import re

def RLE_encode(st:str):
    '''https://www.dcode.fr/rle-compression have bug for 204c'''
    result=''
    
    n = len(st)                               
    bit_len = len(str(n))
    i = 0
    while i < n:

        count = 1
        while (i < n - 1 and 
               st[i] == st[i + 1]):
            count += 1
            i += 1
        result += f"{count}{st[i]}"   #        result += f"{count:0{bit_len}d}{st[i]}"
        i+=1
    return result

def RLE_decode(st:str):
    result=''
    numbers =  list(map(lambda k: int(k),re.findall(r'\d+',st)))
    strings= list(filter(lambda k : k!='',re.sub(r'\d',' ',st).split(' ')))
    
    for i in range(len(numbers)):
        result+=numbers[i]*strings[i]
    return result
    
    

if __name__ == "__main__":
    original = 'ccvvvvv'
    st2='02c05v'
    print(RLE_encode(original))
    print(RLE_decode(st2))
