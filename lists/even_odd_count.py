size=int(input("Enter the size: "))
list_1=[]
even=0
odd=0

for i in range(size):
    element=int(input(f"Enter the element {i+1} :"))
    list_1.append(element)

for i in list_1:
    if i % 2==0:
        even=even+1
    else:
        odd=odd+1

print(f"Number of odd elements in list: {odd}")
print(f"Number of even elements in list: {even}")

#check no of positive and negative elements
zero=0
positive=0
negative=0

for i in list_1:
    if i == 0:
        zero=zero+1
    elif i>0:
        positive=positive+1
    else:
        negative=negative+1

print(f"count of zeros in the list {zero}")
print(f"count of positive numbers in the list: {positive}")
print(f"count of Negative numbers in the list: {negative}")
