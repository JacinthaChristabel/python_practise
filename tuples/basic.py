#Create a tuple with 5 integers and print it.
num=(1,2,3,4,5)
print(num)
print(type(num))

#Create a tuple with different data types (int, float, str, bool).
num_1=(1, 2.3, "hello", True )
print(num_1)

#Print the first element of a tuple.
print(f"first element of num is : {num[0]}")

#Print the last element.
print(f"The last element of num is : {num[-1]}")

#Print the second element.
print(f"Second element of num is: {num[1]}")

#Print the second-last element.
print(f"Second last element of num is : {num[-2]}")

print("For num_1")
print(f"first element of num_1 is : {num_1[0]}")
print(f"The last element of num_1 is : {num_1[-1]}")
print(f"Second element of num_1 is: {num_1[1]}")
print(f"Second last element of num_1 is : {num_1[-2]}")
print(f"Type of True is : {type(num_1[-1])}")

#Find the length of a tuple.
print(f"Length of num is : {len(num)}")
print(f"Length of num_1 is : {len(num_1)}")

#Print all elements using indexing.
for i in range(len(num)):
    print(f"At indexing {i} element is: {num[i]}")

#Print all elements using a for loop.

for i in num:
    print(f" element = {i}")