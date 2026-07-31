#Find the union of two sets
a={1,2,3,4}
b={3,4,5,6}

#method one
res=a.union(b)
print(f"union of a and b is {res}")
#method 2
print(f"union using (|) or operator is {a|b} ")

#Find the intersection of two sets
res_2= a.intersection(b)

#method 1
print(f"Intersection of and b is {res}")
#method 2
print(f"Intersection using (&) and operator {a&b}")

#Find the difference (A - B)
res_3=a.difference(b)
print(f"difference of a and b is {res_3}")
#method 2
print(f"difference of 2 using (-) operator {a-b}")
#method 3 will give elements in B not in A
print(f"elements present in b not in a {b-a}")

#find the symmetric difference.
#a ^ b: Combines elements unique to a and unique to b (removes all shared elements {3, 4})
sy_diff=a.symmetric_difference(b)
print(f"symmetric difference is {sy_diff}")

print(f"symmetric difference using (^)operaation is {a^b}")

#copy set
c=b.copy()
print(f"copied b to c {c}")

#Check whether one set is a subset of another
d = {1, 2}
e = {1, 2, 3, 4}

# Method 1: Using issubset()
print(d.issubset(e))  # Output: True

# Method 2: Using the <= operator
print(d <= e)         # Output: True

#Check whether one set is a supperset of another
print(e.issuperset(d))
print(e >= d)

#Check whether two sets are disjoint.
f={1,2,3}
g={4,5,6}

print(f.isdisjoint(g))  # true because no shared element
h={2,4,5}
print(f.isdisjoint(h))  #false because 2 is shared 

#Convert a list into a set
l=[1,2,3]
s=set(l)
print(type(s))
print(s)

#Convert a tuple into a set
t=(1,2,3)
s=set(t)
print(type(s))
print(s)

