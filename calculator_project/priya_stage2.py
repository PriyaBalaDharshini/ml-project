num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
operator= input("Select operator: (+ or - or / or *): ")
result=''

if operator == "+":
    result=num_1+num_2
    print(f"Addition result:{result}")
elif operator =="-":
    result=num_1-num_2
    print(f"Subtraction result:{result}")
elif operator =="*":
    result=num_1*num_2
    print(f"Multiplication result:{result}")
elif operator =="/":
    if num_2==0:
        print("Error: Division by zero is not allowed")
    else:
        result=num_1/num_2
        print((f"Division result:{result}"))
else:
    print("Invalid operator")
    
if result > 0:
    print("The result number is Positive")
elif result < 0:
    print("The result number is Negative")
else:
    print("The result number is Zero")