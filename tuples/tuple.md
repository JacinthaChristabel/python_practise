# What is a tuple?
-->A tuple is an ordered, immutable (unchangeable) collection of elements in Python,
    defined using parentheses ()

# Difference between list and tuple
-->A list is mutable and defined using square brackets [], whereas a tuple is immutable
    and defined using parentheses ()

# Why are tuples immutable?
-->Tuples are immutable to prevent accidental data changes, optimize memory and execution speed, and 
    allow them to be used as dictionary keys and set elements

# When should you use a tuple instead of a list?
-->Use a tuple when storing fixed, read-only data that shouldn't change, or when we need better memory 
    efficiency and speed

# Why is (5) not a tuple, but (5,) is?
-->In Python, (5) is treated as an integer inside mathematical parentheses, whereas the comma in (5,) tells 
    Python to create a single-element tuple

# Can a tuple contain a list?
-->YES
    eg: t1=(1,2,[1,3,4],5)

While the tuple itself is immutable , the list inside it is still mutable.

  ###Modifying an element inside the list within the tuple
my_tuple[2][0] = 99

print(my_tuple)
 Output: (1, 2, [99, 3, 4], 5)

# How is tuple unpacking used?
-->Tuple unpacking allows you to extract elements of a tuple directly into separate variables in a single line of code.

# Why are tuples faster than lists?
--> Tuples are faster than lists because they are immutable, allowing Python to allocate a fixed memory block and optimize overhead, whereas lists require extra dynamic memory allocation to support sizing operations