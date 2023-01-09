def rsa_encryption(public_key, message) :
    
    '''
    
    Encrypt the given message
    
    '''
    
    return (message ** public_key[1]) % public_key[0]

def rsa_decryption(private_key, dec_message) :
    
    '''
    
    Decrypt the given message
    
    '''
    
    return (dec_message ** private_key[1]) % private_key[0]