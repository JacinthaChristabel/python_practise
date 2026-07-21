#Convert a list into a tuple.
list_1=[1,2,3,4,5]
print(f"Befor conversion : {list_1}")
tuple_1=tuple(list_1)
print(f"After conversion {tuple_1}")
print(f"type after conversion {type(tuple_1)}")

#Convert a string into a tuple.
s1="hello"
print(f"Before conversion :{s1}")
tuple_2=tuple(s1)
print(f"After conversion {tuple_2}")
print(f"type after conversion {type(tuple_2)}")

#Convert a tuple into a set.
tuple_3=(1,2,3,4)
print(f"Before conversion: {tuple_3}")
set_1=set(tuple_3)
print(f"After conversion {set_1}")
print(f"type after conversion {type(set_1)}")

#Convert a set into a tuple.
set_2={1,2,3}
print(f"before conversion {set_2}")
tuple_4=tuple(set_2)
print(f"After conversion {tuple_4}")
print(f"type after conversion {type(tuple_4)}")

#Convert a tuple into a string (using ''.join() for string tuples).
tuple_5=("p","y","t","h","o","n")
res=''.join(tuple_5)
print(res)

#If your tuple contains anything other than strings (like integers or booleans),
#  calling ''.join() directly will throw a TypeError:

#Create a tuple from user input.

size=int(input("Enter the size: "))
my_list=[]

for i in range(size):
    element=int(input(f"Enter element for {i+1}: "))
    my_list.append(element)

print(f"Element in list : {my_list}")

new_tuple=tuple(my_list)
print(f"Tuple contains: {new_tuple}")
print(f"After conversion type is {type(new_tuple)}")

#Create a tuple containing numbers from 1 to 10.

num_tuple=tuple(range(1 , 11))
print(num_tuple)

#Unpack a tuple into three variables
#The number of variables on the left must exactly match the number of items in the tuple.

my_tuple=(1,"red","Apple")
num,colour,fruit= my_tuple
print(f"num is {num}")
print(f"colour is {colour}")
print(f"fruit is {fruit}")

# Single element tuple (must include the trailing comma)
single_tuple = (5,)

print("Tuple:", single_tuple)