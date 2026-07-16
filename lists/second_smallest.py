size = int(input("Enter the size: "))
list_1 = []

for i in range(size):
    element = int(input(f"Enter the element {i+1}: "))
    list_1.append(element)

small = list_1[0]
second_small = float('inf')

for i in list_1:
    if i < small:
        second_small = small
        small = i
    elif i < second_small and i != small:
        second_small = i

print(f"smallest element is: {small}")

if second_small == float('inf'):
    print("Second smallest element does not exist.")
else:
    print(f"Second smallest element is: {second_small}")