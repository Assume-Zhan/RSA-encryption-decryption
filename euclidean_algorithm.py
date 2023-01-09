
def euclidean_algorithm(number_1, number_2, list_1, list_2, remainder = 1) : 
    
    new_pair = [number_1, number_2]
    new_list_1 = list_1
    new_list_2 = list_2
    
    # Select larger number
    if number_1 > number_2 : 
        k = number_1 // number_2
        new_pair[0] = number_1 % number_2
        
        new_list_1[0] = list_1[0] - k * list_2[0]
        new_list_1[1] = list_1[1] - k * list_2[1]
    else : 
        k = number_2 // number_1
        new_pair[1] = number_2 % number_1
        
        new_list_2[0] = list_2[0] - k * list_1[0]
        new_list_2[1] = list_2[1] - k * list_1[1]
        

    if new_pair[0] == 0 or new_pair[1] == 0 :
        return new_pair[0], new_pair[1], new_list_1, new_list_2
    elif new_pair[0] != remainder and new_pair[1] != remainder : 
        return euclidean_algorithm(new_pair[0], new_pair[1], new_list_1, new_list_2, remainder)
    else : 
        return new_pair[0], new_pair[1], new_list_1, new_list_2


def main() :
    a = int(input("Input first number : "))
    b = int(input("Input second number : "))
    
    remainder = int(input("Input wanted remainder : "))
    remainder_1, remainder_2, list_1, list_2 = euclidean_algorithm(a, b, [1, 0], [0, 1], remainder)
    
    if(remainder_1 == remainder) :
        print(remainder, "=", list_1[0], "x", a, "+", list_1[1], "x", b)
    elif(remainder_2 == remainder) :
        print(remainder, "=", list_2[0], "x", a, "+", list_2[1], "x", b)

if __name__ == "__main__" :
    main()