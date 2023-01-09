from rsa_setup import rsa_setup
from rsa_enc_dec import rsa_encryption, rsa_decryption


def main() :
    
    print("Warning : If message is larger than n, it will be module n")
    print("Setup time")
    
    # Setup input
    n = int(input("Input n : "))
    prime_p = int(input("Input prime p : "))
    prime_q = int(input("Input prime q : "))
    e = int(input("Input public key e : "))
    
    # Setup public and private key
    public_key, private_key = rsa_setup(mul_n = n, prime_p = prime_p, prime_q = prime_q, e = e)
    
    # Print private key and public key
    print("Public key   [n, e] : ", public_key)
    print("Private key  [n, d]: ", private_key)
    
    mode = input("Input mode : ")

    
    # Encryption mode
    while(True) :
        if(mode == "enc") : 
            
            message = int()
        
            # Encrypt message
            input_message = input("Message : ")
            
            if(input_message == "exit") : return
            elif(input_message == "chmod") :
                mode = "dec"
                continue
            else : message = int(input_message)
                
            
            enc_message = rsa_encryption(public_key, message)
            
            print("Encrypted message : ", enc_message)
            
            dec_message = rsa_decryption(private_key, enc_message)
            
            print("Original message : ", dec_message)
            
        elif(mode == "dec") : 

                encrypted_message = int()
            
                # Encrypt message
                input_message = input("Encrypted Message : ")
                
                if(input_message == "exit") : return
                elif(input_message == "chmod") :
                    mode = "enc"
                    continue
                else : encrypted_message = int(input_message)
                
                original_message = rsa_decryption(private_key, encrypted_message)
                
                print("Original message : ", original_message)
    

if __name__ == "__main__" :
    main()