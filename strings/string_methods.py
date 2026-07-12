#Convert a string to uppercase
s=input("Enter a string: ")

s1=s.upper()
print(s1)

#Convert a string to lowercase.
s2=s.lower()
print(s2)

#Convert the first letter of each word to uppercase.
s3=s.title()
print(s3)

#Count how many times a character appears in a string.
char=input("Enter a character to find occurance count: ")
count=s.count(char)
print(count)

#Check whether a string starts with "Py".
start_check=s.startswith("Py")
print(start_check)

#Check whether a string ends with ".py".
end_check=s.endswith(".py")
print(end_check)

#Replace all spaces with underscores (_).
s4=s.replace(" ","_")
print(s4)

#Remove leading and trailing spaces.
s5=s.strip()
print(s5)

#Find the position of a given character.
to_find=input("Enter a character to find the position:")
s6=s.find(to_find)
print(f"present in {s6} position")

#Check whether a substring is present in a string.
sub=input("Enter the substring to find in the string: ")

if sub in s:
    print("present")
else:
    print("Not present")