#Find the smallest element without using min().
my_tuple=(1,2,3,4,5)

small=my_tuple[0]

for i in my_tuple:
    if i<small:
        small=i

print(f"smallest is {small}")

#Find the second smallest element without using min().

my_tuple_2=(1,2,3,4,5)

small = my_tuple_2[0]
second_small = float('inf')

for i in my_tuple_2:
    if i < small:
        second_small = small
        small = i
    elif i < second_small and i != small:
        second_small = i

print(f"smallest element is: {small}")
print(f"Second smallest is : {second_small}")