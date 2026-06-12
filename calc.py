while True:
    c=int(input("Enter the choice: "))
    if c==1:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The sum is: ",a+b)
    elif c==2:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The difference is: ",a-b)
    elif c==3:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The product is: ",a*b)
    elif c==4:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The quotient is: ",a/b)
    elif c==5:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The modulus is: ",a/b)
    else:
        print("Invalid choice!")    
        break