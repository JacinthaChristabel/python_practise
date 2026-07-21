#Find the largest element without using max().

my_tuple=(1,2,3,4,5,6)
large=my_tuple[0]

for i in my_tuple:
    if  i > large:
        large= i

print(large)

#Find the second largest element.
my_tuple_2=(1,2,"hello",3,4,5,6,"hi",False)

large=my_tuple_2[0]
second_large=my_tuple_2[0]

for i in my_tuple_2:
    try:
        if i > large:
            second_large = large
            large = i
        elif i > second_large and i != large:
            second_large = i
    except:
        print(f"Skipping non numeric element: {i}")

print(f"Second largest is {second_large}")
        
