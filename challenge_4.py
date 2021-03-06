# challenge_4.py
import os;
import string; 


from challenge_3 import *
from challenge_2 import *
from challenge_1 import *

# 
# use the list(dict) operation to extract a numerablue expression of that dictionaries keys - then loop through to get the values.
# 
#

# within the scope of this task: 
# 1) open file
# 2) convert data to bytes.
# 3) identify the most commonly used value.
# 4) report back a dictionary of the most commonly used value and the data.
# 5) generate an output tool to print the 60 lines that look the closest to making sense.
# SOLUTION EXPRESSION:
# challenge_3.unlock(load_cryptopals("C:\\Local_Code\\repos\\cryptopals_solutions\\set_1\\challenge_4_target\\4.txt")[170],53)
# 
# 170th entry, 60 character string.
# 551be2082b1563c4ec2247140400124d4b6508041b5a472256093aea1847
# ^
# 53
def excessive_force(file_set):
    """ going to run brute-force against many layers
        solution text is "now that the party is jumping\n"
        decrypts on 53, and is successfully identified by a 97 percent readability score
        using challenge_3.unlock(load_cryptopals(file_path)[170],53)
        even with a strange compatibility score.
        returns in the 12 line from file set.
        
        confirming the steps to the 12th line to make sure it is the correct value.
    """
    total_vals = []
    for a in file_set:
        local_vals = []
        if len(a)%2!=0: a = a[:-1]
        b = brute_force(a);
        local_vals = list(b); #get the keys.
        for a_ in (local_vals):
            if char_scoring(b[a_],'ascii',threshold = .97):
                total_vals.append((a_,b[a_],file_set.index(a)));
        #for b in total_vals:
        #    if total_vals.index(b)%3==0: input()
        #    print(b)
        #input()
    # now - I need to run the data from excessive force into a separate value system - getting the 
    # output that makes the most sense.
    # guessed-key(used val?), decrypted value, global position.
    return total_vals;
    
        
        
# looks like .9 would be an appropriate threshold tio use for scanning - at least in my test cases.
# now - I'll only print out those that match the threshold of printability to filter it more thoroughly.
# .99 might be a good indicator for human readability - set it to ceiling on the 100s position...
def char_scoring(binary_string,encoding = 'ascii',threshold = 0.90):
    """
    This mechanism works really surprisingly well for identifying values after the fact to hone in
    on - I can probably work on the steps and scoring later, for sequences that make sense - and
    even more specifically, data that would be in a plaintext.
    
    Build a secondary version that will check and return the match percentage, 
    and offload handling the actual validation to another process.
    
    Determine if a binary string is likely to be valid (Human readable output)
    I'll set some adjustable threshold to determine if the output is 
    
    threshold will be a float - and by default will expect half of all characters
    to be printable.
    
    going to need to programatically score potential hits
    I know I'm looking for plaintext , so values should be in ascii.printable.
    score will be at least 80% of characters are printable.
    
    Alright - while I'm not terribly busy - let's get something to add weight
    based on the percentage of printable characters that are present.
    """
    # handle unusual input for threshold (can't be greater than 1), less than 0 will simply return true.
    if threshold > 1: threshold = 1;
    looks_valid = False;
    a_print = bytes(string.printable,encoding);
    max_ = len(binary_string);
    cnt_ = 0; # I'll take the percentage of printable characters
    for a in binary_string:
        if a in a_print: cnt_+=1;
    if cnt_/max_>=threshold:
        looks_valid = True;
    return looks_valid
    
    
    
def load_cryptopals(file_path):
    """
    open and sanitize the file, will return
    a sequence of records.
    """
    records = []
    with open(file_path,'rb') as cpals:
        x = cpals.readline();
        while x is not None and x != b'':
            if (len(x)%2!=0): x = x[:-1]; # strip the last character if the line is uneven.
            records.append(to_hex(x));
            print(x)
            x = cpals.readline();
    return records; # gets the hashed records. now to pair them with their most likely candidates (brute force if necessary.)
    

def analyze_file(file_contents):
    """
    load data from a file path, and then
    identify the main critical values - one
    of them will make sense.
    
    returns key as position 0 and string as position 2
    """
    load_dict = [];
    for a in file_contents:
        load_dict.append((char_score(a)[0][0],a))# should 
    with open("./scores.txt",'w') as scr:
        scr.write(str(load_dict));    
    return load_dict;
    
def main(file_path):
    recs = load_cryptopals(file_path);
    keys = analyze_file(recs);
    with open("./keys.txt","w") as kys:
        for a in keys:
            kys.write(str(a[0]))
            kys.write("\n");
        
    results = []
    for a in keys:
        results.append(unlock(a[1],a[0]))
    return results
    
if __name__=="__main__":
    file_path = input("Enter the path to breakdown: ");
    res = main(file_path);
    with open(os.path.dirname(file_path)+os.path.basename(file_path)+"solutions.dmp",'wb') as  filepath:
        for a in res:
            filepath.write(a);
            filepath.write(b'\n')
    