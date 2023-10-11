def non_recursive_fibonacci(n):
    a, temp = 0, 0
    b = 1
    if (n == 1) or (n == 2):
        return 1
    elif (n == 0):
        return 0
    elif (n < 0):
        return "Invalid Number"
    else:
        print(a)
        for i in range(n-1): 
            print(b)       
            temp = b
            b = a + b
            a = temp
        # return b

def main():
    n = int(input("Enter Postive Number: "))
    result = non_recursive_fibonacci(n)
    print(f'\n{n}th Fibonacci number: {result}')
    
if __name__ == "__main__":
    main()