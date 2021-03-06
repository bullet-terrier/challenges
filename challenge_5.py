# challenge_5
# REPEATING-KEY XOR

import challenge_4
import challenge_3
import challenge_2
import challenge_1

import sys
import os
import binascii
import string

# FYI - I'm doing this without any help from outside sources - just occasionally referencing the Python help() manual.
# Lock/Unlock Algorithm - I'll generate a lightweight locking mechanism for use 
# >>> for a in targs:
# ...     bits = b''
# ...     with open(a,'rb') as data:
# ...         bits = data.read()
# ...     out = b''
# ...     with open(a,'wb') as data:
# ...         data.write(bytes(repeating_key_cipher(bits,b'password')))
#
# 1) get bytes from plaintext
# 2) get bytes from key
# 3) loop through each byte, looping against each key byte;
#

def repeating_key(key_,len_):
    """
    generate the repeating key of length len_
    use for a padded key
    """
    repeating_key = []
    j = 0;
    k = len(key_);
    while len_ > 0:
        repeating_key.append(key_[j])
        j +=1
        if j >= k: j=0;
        len_-=1;
    return repeating_key

def repeating_key_cipher(plaintext_bytes, key_bytes):
    """
    both values should already be in their base 64 representations.
    Encrypt and decrypt are both handled by this - all that matters is using the 
    same key for both.
    """
    # break the objects into their requisite lists.
    pb = list(plaintext_bytes);
    kb = list(key_bytes);
    # generate an expanded key.
    ek = repeating_key(kb,len(pb));
    crypto_bytes = []
    for i in range(0,len(ek)):
        crypto_bytes.append(pb[i]^ek[i]);
    return crypto_bytes; 

def main():
    """
    """
    set_ = []
    for a in range(1,len(sys.argv)-1,2):
        set_.append(repeating_key_cipher(bytes(sys.argv[a],'utf-16'),bytes(sys.argv[a+1],'utf-16')))
    with open("./output",'wb') as dt: 
        for a in set_:
            dt.write(bytes(a));
            print(a)
    return set_
    
if __name__=="__main__":
    """
    Make sure the key is not equal to the contents...
    that's why these make bad ciphers.
    """
    if len(sys.argv)%2==1 and len(sys.argv)>1: main();
    else:
        print("ctrl+c to exit")
        filename = input("Enter file to decrypt/encrypt: ")
        key = input("enter the plaintext key: ")
        encodint = input("Enter the encoding to use (utf-16/ascii etc.): ")
        data = []
        bits = []
        x = b"";
        if os.path.exists(filename):
            with open(filename,'rb') as bitfile:
                x = bitfile.read();# should be bytes
                writefile = filename
        else: 
            x = bytes(filename,encodint);
            writefile = ("output")
        bits = list(x)
        data = repeating_key_cipher(bytes(bits),bytes(key,encodint))
        with open(writefile,'wb') as fname:
            fname.write(bytes(data))
            print(bytes(data))
            
            
            