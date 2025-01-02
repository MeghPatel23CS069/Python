# problem 1

def isPrime(num) :
    for i in range(2,num) :
        if num%i==0 :
            return None
    return True

def generate_prime(start,end) :
    Prime_numbers=[]
    for i in range(start,end+1) :
        if isPrime(i) :
            Prime_numbers.append(i)
    return Prime_numbers 

print("Prime numbers between 4 and 69 :",generate_prime(4,69))

# problem 2
print("\n")

def flatten(nested_list) :
    flat_list=[]

    for item in nested_list :
        if(isinstance(item,list)) :
            flat_list.extend(flatten(item))
        else :
            flat_list.append(item)
    return flat_list

nested_list = [1 , [1,2] , [1,2,3]]
print("Nested list :",nested_list)
print("Flattened list :",flatten(nested_list))

# problem 3
print("\n")

def find_second_largest(numbers) :

    if len(numbers)<2 : return None

    largest=second_largest= float('-inf')

    for num in numbers :
        if num>largest :
            second_largest=largest
            largest=num
        elif num>second_largest and num!=largest :
            second_largest=num
    
    if second_largest==float('-inf') : return None

    return second_largest

numbers = [-1,-2,68,-99,69,0,88888888888.96]
print("Numbers :",numbers)
print("Second largest number :",find_second_largest(numbers))