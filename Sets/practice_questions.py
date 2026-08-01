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
print(f"unique character in string is : {set(word_3)}")

#revert back to string 
print(f"On reverting back to string : {"".join(word_3)}")

#Convert a set into a sorted list
unsorted_set= {10, 40,39 ,20,5}
sorted_set=sorted(unsorted_set)
print(f"sorted list is {sorted_set}")