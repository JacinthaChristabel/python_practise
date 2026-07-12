s=input("Enter the string: ").lower()
vowel="aeiou"
count=0

for i in s:

    if i in vowel:
        count=count+1

print (count)