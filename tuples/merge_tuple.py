t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

# Merge them using the + operator
merged_tuple = t1 + t2 + t3

print("Merged Tuple:", merged_tuple)
print("Type:", type(merged_tuple))

#Check whether two tuples are equal.

tuple_1=("Hi","hello")
tuple_2=("Hi","hello")
flag=True

if len(tuple_1)!=len(tuple_2):
    print("Two tuples are not equal by length")
else:
    for i in range(len(tuple_1)):
        if tuple_1[i]!=tuple_2[i]:
            print("NOT equal")
            flag=False
            break

if(flag):
    print("Both are equal")
else:
    print("Both are not equal")


#or simply  we can check 

if tuple_1==tuple_2:
    print("EQUAL")
else:
    print("NOT EQUAL")