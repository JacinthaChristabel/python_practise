s=input("Enter a string: ")
vowel="aeiou"
count=0

for i in s:
    if i not in vowel and i.isalpha():
        count=count+1

print(f"number of consonants present in string is {count}")