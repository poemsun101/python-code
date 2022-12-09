s = "good morning"
print("good" in s)
a= "Hello"
print(a[:3]*3)
str=input("str:")
num=int(input("num:"))
if num>len(str)or num<0:
    print("num should be positive,less than length of str")
else:
    print("ressult:",num*str[:num])
a="hello"
a[3]='world'
print(a)



