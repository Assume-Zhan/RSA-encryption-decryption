from euclidean_algorithm import euclidean_algorithm


def isCoprime(number_1, number_2) : 
    
    remainder_1, remainder_2, _ , _ = euclidean_algorithm(number_1, number_2, [1, 0], [0, 1], 0)
    
    if(remainder_1 == 0) :
        if(remainder_2 == 1) : 
            return True
        else :
            return False
    else :
        if(remainder_1 == 1) :
            return True
        else : 
            return False
    

def main() :
    a = int(input("Coprime test number 1 : "))
    b = int(input("Coprime test number 2 : "))
    
    if(isCoprime(a, b)):
        print(a, "and", b, "are coprime")
    else:
        print(a, "and", b, "are not coprime")

if __name__ == "__main__" :
    main()