# challenge_6
import challenge_5
import challenge_4
import challenge_3
import challenge_2
import challenge_1

import os
import sys
import binascii

# hamming difference/number of != bits - 
# probably could do this with an xor
#
#
# challenge dataset 
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
    
def keysize_variance(dataset, min_guess=1,max_guess=8):
    """
    guess the keysize based on the data - find the keysize with the minimum number
    of variations.
    
    returns the best variance, along with some it found along the way...
    """
    assert type(dataset) in (str,bytes,list);
    assert type(min_guess) in (int,float);
    assert type(max_guess) in (int,float);
    minimum_variance  = len(dataset); # set a number greater than the possible variance can be...
    best_guess = max_guess;
    candidates = [];
    for i in range(min_guess,max_guess):
        #if (i>(len(dataset)/2)): break; # precaution against out of whack behaviour.
        # get the slices.
        chunk1,chunk2 = dataset[:i],dataset[i:2*i];
        variance = hamming_string(chunk1,chunk2);
        normal_variance = variance/i
        if normal_variance <= minimum_variance: candidates.append((i,variance/i));
        if normal_variance < minimum_variance: best_guess,minimum_variance = i,variance/i;
    return best_guess,minimum_variance,candidates;
    
def keysize_chunks(dataset,keysize):
    """
    break a dataset into keysized based chunks.
    Designed to be used in conjunction with the 
    keysize_variance function.
    """
    chunks = []
    chunk = []
    for a in range(0,len(dataset)):
        if a>0 and a%keysize==0:
            chunks.append(chunk)
            chunk =[]
        chunk.append(a)
    return chunks;
        
    
def guess_keysize(dataset, min_guess=1,max_guess=100):
    """ friendly output """
    x = keysize_variance(dataset,min_guess,max_guess);
    print("Likely key size: %s\n Minimum variance: %s\n Alternatives: %s"%(x[0],x[1],x[2]))
        
class solution: pass;

solution.keysize = guess_keysize;
solution.data = b''
solution.force_attacks = []
solution.clean_attacks = []
def solution_force(solution):
    for a in range(0,10): solution.force_attacks.append(brute_force(solution.chunks[a]))
def make_clean(solution):
    for a in solution.force_attacks:
        for b in list(a):
            if char_scoring(a[b]): solution.clean_attacks.append((b,a[b])); # append all of the cleaned attacks.