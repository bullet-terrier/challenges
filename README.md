# challenges
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
