import re

def RLE_encode(st):
    result=''
    n = len(st)
    i = 0
    while i < n:

        count = 1
        while (i < n - 1 and 
               st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1 
        result+=str(count)+st[i-1]
    return result
        
def RLE_decode(st:str):
    result=''
    numbers =  list(map(lambda k: int(k),re.findall(r'\d+',st)))
    strings= list(filter(lambda k : k!='',re.sub(r'\d',' ',st).split(' ')))
    
    for i in range(len(numbers)):
        result+=numbers[i]*strings[i]
    return result
        
if __name__ == "__main__":

    st = "aaabb"
    st2='11a2b'
    print(RLE_encode(st))
    print(RLE_decode(st2))
    # RLE_decode(st2)
