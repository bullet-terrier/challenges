# challenge_3.py

"""

challenge 

"""

from challenge_1 import *;
from challenge_2 import *;

import string;

def unlock(input_value,key_int):
    """
    how to actually arrive at the solution (and read it.)
    """
    x = []
    for a in range(0,len(input_value)):
        x.append(key_int);
    x = bytes(x);
    return real_xor(input_value,x);

# define a character scoring mechanism;
# going to try brute force for the hell of it.
def brute_force(single_xor):
    """
    works marvelously - the key to :
    https://cryptopals.com/sets/1/challenges/3
    is byte 88 - in plain english - X (which you'll see by using the ordered list.)
    """
    #single_xor = to_hex(single_xor);
    lens = len(single_xor);
    vals = {}
    for a in range(0,120):# originally 255 - solid bet
        patt = []
        for b in range(0,lens): patt.append(a)
        vals.update({a:real_xor(single_xor,bytes(patt))})
    return vals; # should get the best of the data

def accumulator(input_list):
    """
    take a list, and generate a referential array with the values of a list, associated with
    the number of times they appear in the list.
    
    will work best against sequences with few entries.
    simply gathers all of the values by frequency.
    """
    gen_dict = {}
    for a in input_list:
        gen_dict.update({a:0})
    for a in input_list:
        gen_dict.update({a:gen_dict[a]+1})
    return gen_dict;

def dict_sort(dict_obj):
    srtd = [];
    keys = list(dict_obj.keys());
    while len(dict_obj.keys())>0:
        a = 0;
        while a < len(keys):
            if dict_obj[keys[a]] == max(dict_obj.values()):
                srtd.append((keys[a],dict_obj[keys[a]]))
                dict_obj.pop(keys[a])
                keys = list(dict_obj.keys()); # reset the list;
            a+=1; 
    return srtd;
    
def reverse_order(list_obj):
    """
    return a list in inverted order
    """
    retList = []
    while len(list_obj)>0:
        retList.append(list_obj.pop());
    return retList;
    
def ordered_list(input_scores):
    ret_list = []
    for a in input_scores:
        b = 0;
        while b < a[1]:
            ret_list.append(a[0])
            b+=1
    return ret_list; # should return the ordered values.
    
def char_score(input_string):
    """
    identify which character appears the most frequently, then assign a value to it.
    I'm going to try this with a dict;
    take the setup from the
    """
    scores = accumulator(input_string)
    scores = dict_sort(scores)
    print(scores); # print all of the scores.
    return scores;