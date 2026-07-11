s=input("Enter the string: ")
print(s)

#Print the first half of a string.
half=len(s)//2

print(s[0:half:])

#Print the second half of a string.
print(s[half::])

#Print characters from index 2 to index 7.
print(s[2:8:])

#Print the string except the first character.
print(s[1::])

#Print the string except the last character.
print(s[:-1:])    # or s[:-1]

#Reverse the first five characters.
print(s[4::-1])

#Reverse only the last five characters.
print(s[-1:-6:-1])

#Print every second character.
print(s[::2])

#Print every third character.
print(s[::3])

#Reverse the string using slicing only.
print(s[::-1])