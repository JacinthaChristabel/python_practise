size=int(input("Enter the size: "))
list_1=[]

for i in range(size):
    element=int(input(f"Enter the element {i+1}: "))
    list_1.append(element)

print(f"My list: {list_1}")

large=list_1[0]
small=list_1[0]

for i in list_1:
    if i>large:
        large= i
    if i<small:
        small=i

print(f"largest element is : {large}")
print(f"Smallest element is : {small}")