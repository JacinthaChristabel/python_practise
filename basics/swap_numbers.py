## without using temp variable 

a=int(input("Enter a: "))
b=int(input("Enter b: "))

a,b=b,a

print(f"After swap a is {a} and b is {b}")


##using temp variable

c=int(input("Enter c: "))
d=int(input("Enter d: "))

temp=c
c=d
d=temp

print(f"After swap c is {c} and d is {d}")