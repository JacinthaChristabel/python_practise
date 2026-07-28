#Create a set with five integers and print it.
# A set is an unordered, mutable collection of unique elements

s={1,2,3,4,5,6}
print(s)

#Find the length of a set
print(f"Length of set is {len(s)}")

#Add a new element to a set
s.add(10)
print(s)

#Add multiple elements 
s.update([20,30,40])
print(s)

#Remove an element using remove()
s.remove(20)
print(s)

#Remove an element using discard()
#discard() -> removes the element , if element is not present discard wont give error while remove throws error

s.discard(40)
s.discard(400)  #no error from this line
print(s)

s.pop()  # pop() removes random element from set , pop on empty set throw error
print(s)

#Check whether an element exists in a set
print(3 in s)

#Clear set
s.clear()
print(s)

#note:set() is the only way to create an empty set in Python not this {}