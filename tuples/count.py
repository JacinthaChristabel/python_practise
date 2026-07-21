#Count even and odd numbers in a tuple
my_tuple=(1,2,3,4,"HI",5,6,7,8,9,10,"hello")

even=0
odd=0

for i in my_tuple:
    try:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    except TypeError:
        print(f"Skipping non-numeric element: '{i}'")

print(f"Even count: {even}")
print(f"Odd count : {odd}")

#Count positive and negative numbers.

pos=0
neg=0
for i in my_tuple:
    try:
        if i == 0:
            print("Its zero")
        elif i>0:
            pos=pos+1
        else:
            neg=neg+1
    except:
        print(f"Skipping non numeric element: {i}")

print(f"count of positive number is {pos}")
print(f"count of negative number is {neg}")