#Sum of all the elements in the list

#take user input for list
size=int(input("Enter size: "))
list_1=[]
total=0

for i in range(size):
    element=int(input(f"Enter list element for {i+1}: "))
    list_1.append(element)

# Using Method 
print(f"sum of all elements is {sum(list_1)}")

#using loop
for i in list_1:
    total=total+i

print(f"sum using loop {total}")

#Find the average of all elements.
avg= total//size

print(f"Average of all the elements is {avg}")