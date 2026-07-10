a,b,c=map(int, input("Enter 3 numberes with space between them: ").split())

if (a>=b and a>=c):
    print(f"A is greater {a} ")
elif(b>=a and b>=c):
    print(f"B is greater {b}")
else:
    print(f"C is greater {c}")