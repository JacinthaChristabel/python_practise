size_1= int(input("Enter the size 1 : "))
size_2= int(input("Enter the size 2 : "))
list_1=[]
list_2=[]

for i in range(size_1):
    element=int(input(f"Enter the list_1 element {i+1} : "))
    list_1.append(element)

for i in range(size_2):
    element=int(input(f"Enter the list_2 element {i+1} : "))
    list_2.append(element)

list_3=list_1 + list_2

print(list_3)

list_4=[0]*(size_1+size_2)

for i in range(size_1):
    list_4[i]=list_1[i]

for i in range(size_2):
    list_4[size_1+i]=list_2[i]

print(list_4)
list_4.sort()
print(list_4)