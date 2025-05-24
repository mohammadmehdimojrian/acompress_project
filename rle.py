import re

def RLE_encode(st:str):
    '''https://www.dcode.fr/rle-compression have bug for 204c'''
    result=''
    
    n = len(st)                               
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
    result = ''
    pattern = re.findall(r'(\d+)([a-zA-Z]*)', st)
    # print(pattern)
    for number_str, text in pattern:
        count = int(number_str)
        result += text * count

    return result
    

if __name__ == "__main__":
    original = 'ccvvvvv'
    st2='5a7k'
    print(RLE_encode(original))
    print(RLE_decode(st2))
