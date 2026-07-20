my_tuple=(True,2,"three",4,"five",6)

#Print the first three elements.
print(f"First 3 elements are : {my_tuple[:3:]}")

#Print the last three elements.
print(f"Last 3 elements are: {my_tuple[-3::]}")

#Print elements from index 2 to 5.
print(f"element for 2 to 5 : {my_tuple[2:6:]}")

#Print every alternate element.
print(f"every alternate element is : {my_tuple[::2]}")

#Reverse the tuple using slicing.
print(f"Reverse the tuple using slicing : {my_tuple[::-1]}")

#Print all elements except the first.
print(f"all elements except the first : {my_tuple[1::]}")

#Print all elements except the last.
print(f"all elements except the last : {my_tuple[:-1:]}")

#Print the middle element of a tuple (odd length).

my_tuple_2=(1,2,3,4,5)
lenght=len(my_tuple_2)

if(lenght % 2 != 0):
    print(f"Middle element is {my_tuple_2[lenght//2]}")
else:
    print(f"Length is even")

#Print the first half and second half of a tuple

print(f"first half of tuple is : {my_tuple_2[:lenght//2:]}")
print(f"second half of tuple is : {my_tuple_2[lenght//2::]}")