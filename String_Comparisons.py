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
    while len(bytes_2) < len(bytes_1): bytes_2.append(0); # pad strings to make even. (add null bytes(0) to pad.)
    for a in range(0,len(bytes_1)): total_dist+=hamming_distance(bytes_1[a],bytes_2[a])
    return total_dist;
def hamming_distance(bits_1, bits_2):
    """
    calculate the number of differing bits - should work regardless of
    what format the bytes are in.
    """
    distance = 0;
    val = bits_1 ^ bits_2
    while val > 0:
        distance+=1; # increment the bit counter;
        # set the value and clear a bit. You have to be careful with order of operations in python.
        val = val & (val -1)
    return distance;
hamming_string("a","b")
b = "a"
b = bytes(b,'ascii')
while b>0:
y = 0
while b>0:
    b =b>>1
    y+=1
b = b^0
bytes(0)
bytes('\0')
bytes('\0','ascii')
bytes('\0','ascii') == bytes(0)
bytes(0)
'' != '\x00'
'\x01'^'\x00'
b'\x01'^b'\x00'
b'\x01'^b'\x00'
hamming_string("alpha",'ahpla')
ln = hamming_string("alpha",'ahpla')
5/ln
ln/5
len("alpha")
len("alpha")/hamming_string("alpha","ahpla")
hamming_string("alpha","ahpla")/len("alpha")
2/5(8)
2/(5*8)
10*(2/(5*8))
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
    for a in range(0,len(bytes_in)): total_bits += bit_count(bytes_in);
    return total_bits;
bit_string("alpha")
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
    for a in range(0,len(bytes_in)): total_bits += bit_count(a);
    return total_bits;
bit_string("alpha")
bit_string("a")
bit_string("b")
bit_string("c")
bit_string("c",'utf-16')
bytes('a','ascii')
bytes('a','ascii')
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
x = bit_string('alpha')
x
y = bit_string('ahpla'()
)
y = bit_string('ahpla')
x
y
y = bit_string('zed')
y
hamming_string('ahpla','zed)
hamming_string('ahpla','zed')
y
x/hamming_string('ahpla','zed')
hamming_string('ahpla','zed')/x
hamming_string('ahpla','ahpla')/x
100-(hamming_string('ahpla','ahpla')/x)
100-(hamming_string('ahpla','a')/x)
1(hamming_string('ahpla','a')/x)
1-(hamming_string('ahpla','a')/x)
1-(hamming_string('ahpla','ahpla')/x)
1-(hamming_string('ahpla','alpha')/x)
1-(hamming_string('ahpla','alpha alpha')/x)
1-(hamming_string('ahpla','alphaalpha')/x)
1-(hamming_string('alpha','alphaalpha')/x)
1-(hamming_string('alpha','aahlp')/x)
x
(bit_string('alpha')+bit_string('allph'))/2
(bit_string('alpha')+bit_string('allpha'))/2
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
def string_confidence(bytes_1,bytes_2,encoding = "ascii"):
    """
    calculate the difference in characters between two strings
    returns a percent match between two strings.
    """
    total_percentage=1; # to subtract from.
    length = bit_string(bytes_1)+bit_string(bits_2)/2 # get the average number of bits.
    length = length or 1; # minimum length is 1.
    variance = hamming_string(bytes_1,bytes_2,encoding)
    return total_percentage-(variance/length); # should get the variance we're looking for.
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
def hamming_string(bytes_1,bytes_2,encoding='utf-16'):
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
    while len(bytes_2) < len(bytes_1): bytes_2.append(0); # pad strings to make even. (add null bytes(0) to pad.)
    for a in range(0,len(bytes_1)): total_dist+=hamming_distance(bytes_1[a],bytes_2[a])
    return total_dist;
string_confidence("batman","manbat")
def string_confidence(bytes_1,bytes_2,encoding = "ascii"):
    """
    calculate the difference in characters between two strings
    returns a percent match between two strings.
    """
    total_percentage=1; # to subtract from.
    length = bit_string(bytes_1)+bit_string(bits_2)/2 # get the average number of bits.
    length = length or 1; # minimum length is 1.
    variance = hamming_string(bytes_1,bytes_2,encoding)
    return total_percentage-(variance/length); # should get the variance we're looking for.]
def string_confidence(bytes_1,bytes_2,encoding = "ascii"):
    """
    calculate the difference in characters between two strings
    returns a percent match between two strings.
    """
    total_percentage=1; # to subtract from.
    length = bit_string(bytes_1)+bit_string(bits_2)/2 # get the average number of bits.
    length = length or 1; # minimum length is 1.
    variance = hamming_string(bytes_1,bytes_2,encoding)
    return total_percentage-(variance/length); # should get the variance we're looking for.
string_confidence('batman','manbat')
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
string_confidence('batman','manbat')
string_confidence('batman','Batman')
string_confidence('batman','Bat-man')
string_confidence('batman','Bat Man')
string_confidence('batman','Man- B'aat')
string_confidence('batman','Man- B\'aat')
string_confidence('batman','a t m a n b')
# basically strings matching at about 60 percent are useless
string_confidence('supercalifragilisticexpialidocious','batman')
string_confidence('supercalifragilisticexpialidocious','SuperCalifragilisticexpialidocIous')
string_confidence('supercalifragilisticexpialidocious','SUPERCALIFRAGILISTICEXPIALIDOCIOUS')
string_confidence('supercalifragilisticexpialidocious','1')
string_confidence('supercalifragilisticexpialidocious','BADGER')
# NEED TO RULE OUT WHAT THE DIFFERENCE IS BETWEEN CERTAIN WORDS
string_confidence('supercalifragilisticexpialidocious',string.printable)
import string
string_confidence('supercalifragilisticexpialidocious',string.printable)
string_confidence('supercalifragilisticexpialidocious','')
string_confidence('supercalifragilisticexpialidocious','super')
string_confidence('supercalifragilisticexpialidocious','supercalifragilisticexpialidocious')
def alt_edit_confidence(bytes_1,bytes_2,encoding = 'ascii'):
    """"""
    total_percentage = 1;
    length = bit_string(bytes_1) # not adjusting for the longer string, just seeing what happens.
    variance = hamming_string(bytes_1,bytes_2,encoding);
    return total_percentage-(variance/length);
alt_edit_confidence('supercalifragilisticexpialidocious,'supercalifragilisticexpialidocious')
alt_edit_confidence('supercalifragilisticexpialidocious','supercalifragilisticexpialidocious')
alt_edit_confidence('supercalifragilisticexpialidocious','super')
alt_edit_confidence('super','supercalifragilisticexpialidocious')
