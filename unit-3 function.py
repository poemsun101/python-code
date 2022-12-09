def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("sum : " , a+b)
def sub():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("substraction : " , num1-num2)
def multiplication():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    c = num1*num2
    return(c)


add() # function call
sub()
result = multiplication()
print("multiplication answer: " , result)