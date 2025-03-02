num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))

option = int(input("Chosen to the operator: "))
if option in [1,2,3,4]:

    if option ==1:
        print("Substract:",num1 + num2)

    elif option ==2:
        print("Differance: ",num1 - num2)

    elif option ==3:
        print("Multiply: ",num1 * num2)

    elif option ==4:
        print("Divide:",num1 / num2)

    else:
        print("Error")

