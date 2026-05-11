def main():
    alg = input ("Please, enter 1 to create a check digit, or enter 2 to verify a number: ")
    if alg=="1":
        check_digit()
    elif alg =="2":
        verify()
    else:
        print ("Please enter a valid number")
        main() #restart
        
def check_digit():
    number = input("Please, enter the number you want to have a check digit for: ")
    digits = [int(d) for d in str(number)]
    n = len(digits)
    
    if n%2==0:
        result = order(digits[:], 1, n)
    else:
        result = order(digits[:], 0, n)

    check_digit = (10 - (sum(result)%10))%10
    #double mod 10 to prevent check digit from becoming 10 instead of 0
    
    print(f"The check digit for the number you provided is: {check_digit}")
    print(f"Full number: {number}{check_digit}")
    
def order(digits, beg, end):
    #replace every other digit with its substiitution
    for i in range (beg, end, 2):
       digits[i] = substitution(digits[i])
    return digits
    
        
def substitution(digit):
    digit = digit*2
    if digit>9:
        return sub_sub(digit)
    else:
        return digit
        
def sub_sub(dig):
    return (dig//10) + (dig%10)
    
def verify():
    number = input("Please, enter the number you want to verify: ")
    digits = [int(d) for d in str(number)]
    n = len(digits)

    if n%2==0:
        result = order(digits[:], 0, n)
    else:
        result = order(digits[:], 1, n)
   
    total_sum = sum(result)%10  
    
    if total_sum==0:
        print("Your number is veriied!")
    else:
        print ("Your number couldn't be verified.")

if __name__ =="__main__":
    main()
