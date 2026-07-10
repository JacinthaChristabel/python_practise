num=int(input("Enter number: "))
num2=0
while num>0:
    rev=num%10
    num2=num2*10+rev
    num=num//10

print(num2)