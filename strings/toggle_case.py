s=input("Enter the string: ")
result=""

for i in s:
    if (i >= 'A') and (i<='Z'):         #Or i can use built in isupper to check
        result=result+i.lower()
    elif(i>='a') and (i<='z'):           #or built in islower 
        result=result+i.upper()
    else:
        result = result + i
print(result)
