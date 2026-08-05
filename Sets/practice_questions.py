#Remove duplicate elements from a list using a set
l=[1,1,2,3,4,3]
s=set(l)
print(s)

#Find the common elements between two lists using sets
l1=[1,2,3,5,7,8,0]
l2=[1,2,3,4,5,6,7]

s1=set(l1)
s2=set(l2)
# Common elements (Intersection)
common=s1.intersection(s2)
print(f"common elements are {common}")

#Find elements present in the first list but not in the second
print(f"Elements present in s1 not in s2 : {s1-s2}")

#Find elements present in either list but not both (symmetric)
print(f"symmetric difference is : {s1^s2}")

#Merge two set
print(f"s1 + s2 = {s1|s2}")  #union 

#Count the number of unique elements in a list.
print(f"print count of unique elements in set 1 is : {len(s1)}")

# Check whether two sets are equal.
print(f"S1 is equal to s2 : {s1==s2}")

# Find the maximum element in a set.
print(f"Maximum element in s1 is: {max(s1)}")

# Find the minimum element in a set
print(f"Minimum element in s1 is: {min(s1)}")

# Find the sum of all elements in a set
print(f"Sum of all elements in s1 is: {sum(s1)}")

#Find the average of all elements in a set
print(f"Average of elements in set 1 : {(sum(s1)//len(s1))}")

#Take a sentence as input and print all unique words
sentence="hello world good morning hello world"
word=sentence.split()
unique_word=set(word)
print(f"Unique word in sentence is {unique_word}")

#Count the number of unique characters in a string
word_2="hello"
unique_char=set(word_2)
print(f"unique character in the word is : {unique_char}")

#Remove duplicate characters from a string using a set
word_3="hellooo hiii "
unique=set(word_3)
print(f"unique character in string is : {unique}")

#revert back to string 
print(f"On reverting back to string : {"".join(unique)}")

#Convert a set into a sorted list
unsorted_set= {10, 40,39 ,20,5}
sorted_set=sorted(unsorted_set)
print(f"sorted list is {sorted_set}")

#Check if an element is not present in a set.
set_1={1,20,2,3}
print(200 not in set_1)

#Find the size of the union of two sets
#Find the size of the intersection of two sets
a={1,2,3,5,7}
b={1,2,4,6,8,9} 

a1=a.union(b)
b1=a.intersection(b)
print(f"length of a union with b : {len(a1)}")
print(f"length of b intersection with a : {len(b1)}")

#Remove all common elements from two sets
res=a.symmetric_difference(b)
print(f"Removing all common elements from two sets: {res}")

#Find whether two lists have at least one common element using sets
c={1,2}
d={3,4}

if len(c&d) >= 1:
    print("Two sets have atleast one common element")
else:
    print("Two sets dont have common element")

#Find duplicate values in a list using a set
dup=[1,1,2,2,3,3,4,5]
seen=set()
dup_l=set()

for i in dup:
    if i in seen:
        dup_l.add(i)
    else:
        seen.add(i) 

print(f"duplicate elements are : {dup_l}")

#Find all unique vowels in a string
string="hellohelloworld"
vowel="aeiou"

# Simple set intersection
unique_vowels = set(string)& set(vowel)
print(f"unique vowels are : {unique_vowels}")  # Output: {'e', 'o'}

#method 2
seen=set()
unique_vowel=set()

for i in string:
    if i in vowel:
        if i not in seen:
            unique_vowel.add(i)
        else:
            seen.add(i)

print(unique_vowel)

#Find unique words in two different sentences
line_1="hello world"
line_2="my name is name"

s_line1=set(line_1.split())
s_line2=set(line_2.split())
result=s_line1 | s_line2
print(f"result is {result}") 

#Check whether all elements of one set exist in another

s_1={1,2,3}
s_2={1,2,3}

if s_1.issubset(s_2):
    print("All elements are present")
else:
    print("NO")

# Creating a frozenset from a list and print it
numbers = frozenset([1, 2, 3, 4, 4])

print(numbers)        # Output: frozenset({1, 2, 3, 4})
print(type(numbers))  # Output: <class 'frozenset'>

#Frozen set is a immutable set , trying to modify the frozenset will lead to attribute error