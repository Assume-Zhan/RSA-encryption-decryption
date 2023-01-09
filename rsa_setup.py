from euclidean_algorithm import euclidean_algorithm
from coprime import isCoprime
from prime_factorization import prime_factorization

def rsa_setup(mul_n = -1, prime_p = -1, prime_q = -1, e = -1) : 
    
    '''
    
    Get two primes : p and q and calculate n = p * q
    Generate e or given e for public key : [n, e]
    Generate d by : e * d % phi(n) = 1
    
    Be careful : 
        - p and q must be prime
        - e must coprime to phi n 
    
    Return public key pair and private key pair
    
    '''
    
    n = int()
    phi_n = int()
    if(mul_n != -1) :
        
        primes = prime_factorization(mul_n)
        
        if(len(primes) != 2) : return "Failed"
        
        new_prime_p = primes[0]
        new_prime_q = primes[1]
        n = new_prime_p * new_prime_q
        
        # Calcullate phi n
        phi_n = (new_prime_p - 1) * (new_prime_q - 1)
    else :
        n = prime_p * prime_q
        
        # Calcullate phi n
        phi_n = (prime_p - 1) * (prime_q - 1)
    

    
    # Find public key : e
    if(e == -1) : 
        # Find proper e, s.t. e is coprime to phi_n
        for i in range(2, phi_n) : 
            if(isCoprime(phi_n, i)) : 
                e = i
                break
        else : e = 2
        
    # Find private key : d
    d = int()
    remainder_1, remainder_2, list_1, list_2 = euclidean_algorithm(e, phi_n, [1, 0], [0, 1], 1)
    if(remainder_1 == 1) :
        d = list_1[0]
    else :
        d = list_2[0]
        
    
    return [n, e], [n, d]

def main() :
    n = int(input("Input n : "))
    prime_p = int(input("Input prime p : "))
    prime_q = int(input("Input prime q : "))
    e = int(input("Input public key e : "))
    
        
    print(rsa_setup(mul_n = n, prime_p = prime_p, prime_q = prime_q, e = e))

if __name__ == "__main__" : 
    main()