#challenge_2.py
from challenge_1 import *;

# use what you've done, no?

def real_xor(input_bytes1, input_bytes2):
    """
    handle the real xor - from data already in hex form.
    https://cryptopals.com/sets/1/challenges/2
    this is what the code meant.
    """
    output_array = []
    if len(input_bytes1)==len(input_bytes2):
        for a in range(len(input_bytes1)):
            try:
                output_array.append(input_bytes1[a]^input_bytes2[a]);
            except Exception as echo:
                print(echo)
    return bytes(output_array);
    
def fixed_xor(input_string1,input_string2):
    """
    https://cryptopals.com/sets/1/challenges/2
    
    depends upon hex_to_b64;
    
    I think I basically had this right initially - base encoding in python
    is surprisingly frustrating since it tries to convert everything to a different base.
    
    Converts the ascii representation of the hexadecimal hash, then converts it to the what it represents, then returns the xor.
    this just handles the input more nicely.
    """
    output_string = bytes();
    output_array = [] # should be an array of bytes... dynamic typing is a bit frustrating...
    if len(input_string1)==len(input_string2):
        # always scrub with to_hex for these inputs.
        input_string1,input_string2 = to_hex(input_string1),to_hex(input_string2); # try without the hex...
        for a in range(len(input_string1)):
            try:
                #output_string+=bytes(input_string1[a]^input_string2[a]);
                output_array.append(input_string1[a]^input_string2[a])# generate the xor values.
                #print(bytes(input_string1[a]^input_string2[a]))
            except Exception as echo:
                output_array.append(input_string1[a]^input_string2[a]);
                print(echo);
            #if len(output_array) > 0:
            #    output_string = bytes(output_array);
        print(output_array);
    return bytes(output_array);# alright keep in mind it will look like a string, but we really care about the underlying data.