size=int(input("Enter size"))
list_1= []

for i in range(size):
    element=input(f"Enter the list element {i+1}: ")
    list_1.append(element)

print(f"elements you entered are {list_1}")

#Print the first three elements.
print(f"First 3 elements : {list_1[:3:]}")

#Print the last three elements.
print(f"Last 3 elements: {list_1[-3::]}")

#Print elements from index 2 to 5.
print(f"elements for 2 to 5 index: {list_1[2:5:]} ")

#Print all elements except the first.
print(f"except first element: {list_1[1::]}")

#Print all elements except the last.
print(f"except last element: {list_1[:-1:]}")

#Print all elements except the last 2 .
print(f"except last 2 element: {list_1[:-2:]}")

#Reverse the list
print(f"Reverse: {list_1[::-1]}")

#Print every second element.
print(f"every 2nd element: {list_1[::2]}")

#Print every third element.
print(f"every 3nd element: {list_1[::3]}")

#Print the middle element (odd-length list)
middle=len(list_1)
if (middle %2 !=0):
    print(f"middle element is {list_1[middle//2]}")
else:
    print("List length is even ")

#Print the first half and second half of the list.
print(f"first half {list_1[:middle//2:]}")
print(f"second half {list_1[middle//2::]}")