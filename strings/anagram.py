s=input("Enter the string: ").lower()
s2=input("Enter the 2nd string: ").lower()


if sorted(s)== sorted(s2):
    print("Anagram")
else:
    print("Not a Anagram")