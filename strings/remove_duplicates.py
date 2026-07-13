s=input("Enter the string: ")
result=""

for i in s:
    if i not in result:
        result=result+i

print(f"After removing duplicates: {result}")