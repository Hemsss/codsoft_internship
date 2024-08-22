def calculator():
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

   
    operation = int(input("Enter the operation (1/2/3/4/5): "))

    
    if operation == 1:
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == 2:
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == 3:
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == 4:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    elif operation == 5:
        result = num1% num2
        print(f"The result of {num1} % {num2} is: {result}")
    else:
        print("Invalid operation.")


calculator()
