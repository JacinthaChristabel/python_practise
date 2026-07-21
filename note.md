note:
A for loop can only iterate over iterable objects such as:
 range()
 list
 tuple
 string
 dictionary
 set


*Strings cannot be modified after they are created.


*Since tuples are immutable in Python, they cannot be modified after creation and do not support methods like .append(). To handle dynamic user input, it is best practice to collect the data in a list first and then convert it into a tuple using the tuple() constructor.

*Tuple unpacking allows you to extract elements of a tuple directly into separate variables in a single line of code.