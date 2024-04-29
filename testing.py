name = input("Enter Username: ")
print("Hello", name)
first = float(input ("Enter first number: "))
second = float(input("how much you would like to add?: "))
while True:
    third = input("would you like to add, subtract, multiply or divide: ")
    if third == "add":
        print("answer is: ", float(first + second))
        break
    elif third == "subtract":
        print("answer is: ", float(first - second))
        break
    elif third == "divide":
        print("answer is: ", float(first / second))
        break
    elif third == "multiply":
        print("answer is: ", float(first * second))
        break
    else: 
        print("Invalid; please enter add, subtract, divide or multiply")


    