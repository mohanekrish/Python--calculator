print("       Calculator      ")

a=int(input("enter a:"))
b=int(input("enter b:"))

print("choose operation")
print("1.addition")
print("2.Subtract")
print("3.Multiplication")
print("4.division")

op =(input("Enter operation(1-4):"))

match op:
    case "1":
        print("sum = ", a+b)
    case "2":
        print("Sub = ",a-b)
    case "3":
        print("Mul = ",a*b)
    case "4":
        if b != 0:
            print("Div = ",a/b)
        else:
            print("divisible by zero is not allow")
    case _:
        print("Invalid user")
