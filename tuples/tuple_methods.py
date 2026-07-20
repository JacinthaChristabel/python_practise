my_tuple=(True,2,"three",4,"five",6,True,2,6,2)

#Count how many times an element appears using count().
element_input=input("Enter the element whos count need to be found: ")

if element_input.isdigit():
    element=int(element_input)
elif(element_input=="True"):
    element=True
elif(element_input=="False"):
    element=False
else:
    element=element_input

print(f"count of {element} is my_tuple is : {my_tuple.count(element)}")

#Find the index of an element using index().

my_tuple_2=(1,2,3,4,5)
print(f"tuple elements are : {my_tuple_2}")
ele=int(input("Enter the element who s index need to be found: "))
print(f"The index of {ele} is {my_tuple_2.index(ele)}")

#Check whether an element exists in a tuple.
num=int(input("Enter the element to check existance: "))

if num in my_tuple_2:
    print(f"{num} is present in the list")
else:
    print(f"{num} is not present in the list")

#Concatenate two tuples.
tuple_1=("hello",)
tuple_2=("World",)

tuple_1=tuple_1+tuple_2
print(tuple_1)

#Repeat a tuple three times using *.
print(tuple_1 *3)

#Find the maximum element.
print(f"largest element is: {max(my_tuple_2)}")

#Find the minimum element.
print(f"smallest element is: {min(my_tuple_2)}")

#Find the sum of all elements.
print(f"sum of all the elements in tuple is : {sum(my_tuple_2)}")

#Find the average of all elements.
print(f"average of tuple is : {(sum(my_tuple_2))//len(my_tuple_2)}")

#Convert a tuple to a list.

tuple_3=(1,2,3)

list_1=list(tuple_3)
print(f"after conversion of tuple to list : {list_1}")
print(f"the type is {type(list_1)}")