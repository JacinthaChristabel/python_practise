s=input("Enter the string: ")
repeated=None

seen=""
#finding first repeated character

for i in s:
    if i in seen:
        repeated=i
        break
    else:
        seen=seen=i

if(repeated):
    print(f"The repeated character is {repeated}")
else:
    print("There are no repeated characters ")