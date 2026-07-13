#Method one
s=input("Enter the string: ")
first=0
last=len(s)-1
flag=True

while first< last:
    if s[first] == s[last]:
        first=first+1
        last=last-1

    else:
        flag=False
        break

if(flag):
    print("Palindrome")
else:
    print("Not a palindrome")


#Method 2

print ("Method 2 result: ")

s2=s[::-1]
print(s2)

if s==s2:
    print("Palindrome")
else:
    print("Not a palindrome")
