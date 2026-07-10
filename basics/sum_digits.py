num=int(input("Enter number: "))
count=0
while num>0:
    rev=num%10
    count=count+rev
    num=num//10

print(count)

