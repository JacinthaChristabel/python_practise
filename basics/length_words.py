s1 , s2= input("Enter 2 words with space between them: ").split()

if (len(s1)==len(s2)):
    print("both strings are equal in length")
elif(len(s1)>len(s2)):
    print("string1 is longer")
else:
    print("string 2 is longer")