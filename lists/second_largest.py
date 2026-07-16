size = int(input("Enter the size: "))
list_1 = []

for i in range(size):
    element = int(input(f"Enter the element {i+1}: "))
    list_1.append(element)

large = list_1[0]
second_large = float('-inf')

for i in list_1:
    if i > large:
        second_large = large
        large = i
    elif i > second_large and i != large:
        second_large = i

print(f"Largest element is: {large}")

if second_large == float('-inf'):
    print("Second largest element does not exist.")
else:
    print(f"Second largest element is: {second_large}")