size=int(input("Enter the size: "))
list_1=[]

for i in range(size):
    element=input(f"Enter the element {i+1}: ")
    list_1.append(element)

if len(list_1)>0:
    rotated_left=list_1[1:]+[list_1[0]]       ##Rotate a list to the left by one position.
    rotated_right=[list_1[-1]]+list_1[:-1]   #Rotate a list to the right by one position.

print(rotated_left)
print(rotated_right)