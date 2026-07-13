s1=input("Enter string1: ")
s2=input("Enter string 2: ")
flag=False

if len(s1)!=len(s2):
    print("String are not same length")
    flag=True
else:
    for i in range (len (s1)):
        if s1[i]!=s2[i]:
            flag=True
            break

if(flag==False):
    print("two strings are same")
else:
    print("not same")


#method 2

print("Method 2")

if s1== s2:
    print ("Same string")
else:
    print("Different string ")