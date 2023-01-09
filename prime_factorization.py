
def prime_factorization(n) : 
    
    primes = []
    
    current_prime_fac = 2
    current_n = n
    while(n > current_prime_fac) : 
        if(current_n % current_prime_fac != 0) :
            current_prime_fac = current_prime_fac + 1
        else :
            current_n = current_n / current_prime_fac
            primes.append(current_prime_fac)
            
    return primes

def main() :
    x = int(input("Input the number : "))
    print(prime_factorization(x))
    
if __name__ == '__main__' :
    main()