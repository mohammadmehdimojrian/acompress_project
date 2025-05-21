class Nodetree():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return f'{self.left}      {self.right}'


def first_father(nodes: list):
    while len(nodes) > 1:
        key1, c1 = nodes[0]
        key2, c2 = nodes[1]
        nodes = nodes[2:]
        node = Nodetree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1])
    return nodes[0][0]  


def freq_letter(st: str):
    nodes = {}
    for char in set(st):
        nodes[char] = st.count(char)
    return sorted(nodes.items(), key=lambda k: k[1])


def huffman_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    if isinstance(node, str):  #leaf
        codebook[node] = prefix
    else:
        left, right = node.children()
        huffman_codes(left, prefix + '0', codebook)
        huffman_codes(right, prefix + '1', codebook)
    return codebook


def huffman_encode(string: str):
    if len(list(set(string)))==1:
        return len(string) *'1' , {string[0]:'1'}
    nodes = freq_letter(string)
    root = first_father(nodes)
    codebook = huffman_codes(root) #{'E': '000', 'C': '001', 'B': '01', 'A': '10', 'w': '110', 'F': '111'})

    encoded = ''.join(codebook[char] for char in string)
    
    return encoded , codebook

def huffman_decode(encoded , codebook):
    decoded=''
    cur=''
    for bit in encoded:
        cur+=bit
        for c,b in codebook.items():
            if cur == b:
                decoded+=c
                cur=''
                break
    print(decoded)

if __name__ == '__main__':
    string = 'aaaaaaa'
    encoded_string , codebook = huffman_encode(string)
    print(encoded_string , list(codebook.items()))
    huffman_decode(encoded=encoded_string , codebook=codebook)
    
