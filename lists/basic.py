#Create a list of five numbers and print it.
list_1=[1,2,3,4]
print(list_1)

#Take user input for the list
list_2=[]
n=int(input("Enter the size of list: "))

for i in range (n):
    element=int(input(f"Enter the list element for {i+1}: "))
    list_2.append(element)

print(list_2)

#Print the first element.
print(f"first element is {list_2[0]}")

#Print the last element.
print(f"Last element is {list_2[-1]}")

#Print the second element.
print(f"Second element is {list_2[1]}")

#Print the second-last element.
print(f"The second-last element is {list_2[-2]} ")

#Find the length of a list.
print(f"length of list is {n}")
print(f"length of the list is {len(list_2)}")

#Print all elements using indexing.
print("All the elements in the list are : ")
for i in range(len(list_2)):
    print(list_2[i])

#Print the list in reverse using slicing.
print(list_2[::-1])

#Print every alternate element.
print(list_2[::2])