size=int(input("Enter the size: "))
list_1=[]
res=[]

for i in range(size):
    element=input(f"Enter the element {i+1}: ")
    list_1.append(element)

for i in list_1:
    if i not in res:
        res.append(i)

print(res)