s=input("Enter the string: ")
u_count=0
l_count=0
d_count=0
s_count=0

#alnum
#It contains only alphabet letters (h, p, o, w).
#There are no spaces, punctuation marks, or special characters.

if s.isalnum():
    print("Entered string is a alphanumeric")
else:
    print("Entered string is no a alphanumeric")

for i in s: 
    if i.isupper():
        u_count=u_count+1
    elif i.islower():
        l_count=l_count+1
    elif i.isdigit():
        d_count=d_count+1
    elif i.isspace():
        s_count=s_count+1
    else:
        print("Special character ")

print(f"count of uppercase in string is {u_count}")
print(f"count of lowercase in string is {l_count}")
print(f"count of digit in string is {d_count}")
print(f"count of space in string is {s_count}")