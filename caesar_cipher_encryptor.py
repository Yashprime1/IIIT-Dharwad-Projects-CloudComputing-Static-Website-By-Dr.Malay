import Algorithmia

import jsons


# All basic necessity global values defined over here  
letter_number_mapping={
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25, 
}
number_letter_mapping={
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z', 
}

# For Caeser Cipher , the K value is 3 but the following is a general implementation for any K
def caeser_cipher_encryption(P,K):
    # initializing variables of use
    C=""
    print(P)
    print(K)
    P=P.lower()
    K=int(K)
    for i in range(len(P)):
        if(P[i] not in letter_number_mapping):
            C=C+P[i]
        else:

            C=C+number_letter_mapping[(letter_number_mapping[P[i]]+K) % 26]
    return C  
    
    

    
    
  




def apply(input):
    input=input.split('**')
    result=caeser_cipher_encryption(input[0],input[1])
    return result

