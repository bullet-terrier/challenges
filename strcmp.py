#

def hamming_distance(bits_1, bits_2):
    """
    calculate the number of differing bits - should work regardless of 
    what format the bytes are in.
    """
    distance = 0;
    val = bits_1 ^ bits_2
    while val > 0:
        distance+=1;
        val = val & (val -1)
    return distance;

def hamming_string(bytes_1,bytes_2,encoding = 'utf-16'):
    """
    calculate the total hamming difference from a set of strings...
    
    identical strings should return a zero.
    """
    total_dist = 0;
    assert type(bytes_1) in (str,bytes,list)
    assert type(bytes_2) in (str,bytes,list)
    if type(bytes_1) == str: bytes_1 = bytes(bytes_1,encoding)
    if type(bytes_2) == str: bytes_2 = bytes(bytes_2,encoding)
    if type(bytes_1) == bytes: bytes_1 = list(bytes_1);
    if type(bytes_2) == bytes: bytes_2 = list(bytes_2);
    if len(bytes_2)>len(bytes_1): bytes_1,bytes_2 = bytes_2,bytes_1;
    while len(bytes_2) < len(bytes_1): bytes_2.append(0); # pad strings to make even.
    for a in range(0,len(bytes_1)): total_dist+=hamming_distance(bytes_1[a],bytes_2[a])
    return total_dist;

def string_confidence(bytes_1,bytes_2,encoding = "ascii"):
    """
    calculate the difference in characters between two strings
    returns a percent match between two strings.
    """
    total_percentage=1; # to subtract from.
    length = bit_string(bytes_1)+bit_string(bytes_2)/2 # get the average number of bits.
    length = length or 1; # minimum length is 1.
    variance = hamming_string(bytes_1,bytes_2,encoding)
    return total_percentage-(variance/length); # should get the variance we're looking for.
   
def alt_edit_confidence(bytes_1,bytes_2,encoding = 'ascii'):
    """"""
    total_percentage = 1;
    length = bit_string(bytes_1) # not adjusting for the longer string, just seeing what happens.
    variance = hamming_string(bytes_1,bytes_2,encoding);
    return total_percentage-(variance/length);

def bit_string(bytes_in,encoding='ascii'):
    """
    handler for capturing and returning the bit length.
    remember that this will count NON ZERO BITS. You may get
    some odd behaviour in utf-16 encoded strings.
    """
    total_bits  = 0;
    ### type conversion components ###
    assert type(bytes_in) in (str,bytes,list) # don't want to get a type error.
    if type(bytes_in) == str: bytes_in  = bytes(bytes_in,encoding);
    if type(bytes_in) == bytes: bytes_in = list(bytes_in) # needs to be a list.
    ###    END TYPE CONVERSION!    ###
    for a in range(0,len(bytes_in)): total_bits += bit_count(bytes_in[a]);
    return total_bits;

def bit_count(a,b=0x01):
    """ count number of active bits in an object
        Needs to follow the same pattern of use
        as hamming string and hamming distance.
        this is incredibly encoding dependent - so be warned.
    """
    c = 0;
    while a>0:
        a = a>>b;
        c+=1;
    return c

def main():
    print(__name__);
    test_cases()
    input();


def test_cases():
    input(str(string_confidence('batman','manbat')))
    input(str(string_confidence('batman','Batman')))
    input(str(string_confidence('batman','Bat-man')))
    input(str(string_confidence('batman','Bat Man')))
    input(str(string_confidence('batman','Man- B\'aat')))
    input(str(string_confidence('batman','Man- B\'aat')))
    input(str(string_confidence('batman','a t m a n b')))
    # basically strings matching at about 60 percent are useless
    input(str(string_confidence('supercalifragilisticexpialidocious','batman')))
    input(str(string_confidence('supercalifragilisticexpialidocious','SuperCalifragilisticexpialidocIous')))
    input(str(string_confidence('supercalifragilisticexpialidocious','SUPERCALIFRAGILISTICEXPIALIDOCIOUS')))
    input(str(string_confidence('supercalifragilisticexpialidocious','1')))
    input(str(string_confidence('supercalifragilisticexpialidocious','BADGER')))
    
if __name__=="__main__":
    pass;
    main()
    
if __name__!="__main__":
    pass;
