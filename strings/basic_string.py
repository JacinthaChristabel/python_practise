#Take a string as input and print it.
name=input("Enter your name: ")
print(type(name))
print(name)

#Find the length of a string.
length=len(name)
print(length)

#Print the first character of a string.
first=name[0]
print(first)

#Print the last character of a string.
print(name[-1])

#Print the second character.
print(name[1])

#Print the second last character.
print(name[-2])

#Print the first five characters.
print(name[0:5:])

#Print the last five characters.
print(name[-5::])

#Print the string in reverse
name2=name[::-1]
print(name2)

#Print every alternate character.
print(name[::2])