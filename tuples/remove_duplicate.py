#Remove duplicates by converting the tuple to a set, then back to a tuple.

my_tuple=(1,2,7,4,"HI",4,2,7,"HI")
#Convert tuple to set (removes duplicates automatically)
my_tuple=set(my_tuple)
print(my_tuple)
print(type(my_tuple))


#methnd 2 manually using list
print("method 2")
t2=(1,2,7,4,"HI",4,2,7,"HI")
l=[]

for i in t2:
    if i not in l:
        l.append(i)

print(f"list after duplicate removal : {l}")
t2=tuple(l)
print(f"list converted to tuple: {t2}")