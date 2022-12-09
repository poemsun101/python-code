def squares(x):
    return x**2
list1=[1,2,3,4,5]
# using the squres func inside map function
print(list(map(squares,list1)))
# using the lambda func inside map function
print(list((squares,list1)))

print(list(map(lambda x: x ** 2, list1)))
# using list comprehension to get equivalent as map
print([x ** 2 for x in list1])

#filter function
a = [1,2,3,4,5,7,9]
b = [2,3,6,7,9,8]
print(list(filter(lambda x: x not in a,b)))
print([x for x in a if x in b])

def largestinthree(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
num1 = int(input("Please enter a value for num1:"))
num2 = int(input("Please enter a value for num2:"))
num3 = int(input("Please enter a value for num3:"))
result = largestinthree(num1,num2,num3)
print("largest of the value entered is",result)

def computeGCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0) and (y%i==0):
            gcd=i
    return gcd
a = int(input("x:"))
b= int(input("y:"))
print(computeGCD(A,B))