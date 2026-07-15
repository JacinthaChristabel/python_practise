size=int(input("Enter the size: "))
list_1=[]

for i in range(size):
    element=input(f"Enter list element {i+1} : ")
    list_1.append(element)

#Append an element.
list_1.append("100")
print(list_1)

#Insert an element at a given position.
ele=input("Enter the element to insert: ")
pos=int(input("Enter the position to insert: "))

list_1.insert(pos, ele)
print(list_1)

#nested list

list_2=[1,2,3,4,5]
list_3=["apple", "orange","500"]

#.append() treats the second list as a single item. It drops the entire container inside:[1, 2, 3, 4, 5, ['apple', 'orange', '500']]
list_2.append(list_3)     
print(f"after appending list 2 and list 3 : {list_2}")

#Extend one list with another.
list_4=[1,2,3,4,5]
list_5=["apple", "orange","500"]
list_4.extend(list_5)
print(f"after extending list 4 and list 5 : {list_4}")

#.extend() unpacks the second list first, then adds its individual elements one by one:[1, 2, 3, 4, 5, 'apple', 'orange', '500']

#Remove an element by value. 
list_3.remove("orange")
print(f"After remove orange from list 3 : {list_3}")

#Remove an element by index using pop().
list_6=[10,20,30,40]
print(f"before pop list_6 has : {list_6}")
list_6.pop(2)
print(f"After 2nd index pop : {list_6}")

#Clear the list.
list_6.clear()

print(f"After clearing list_6 : {list_6}")

#Find the index of an element.
list_7=["hi", "hello", "how", "are", "you", "200"]
print(f"list_7 contains: {list_7}")
to_find=input("Enter the element whos index needss to be found: ")

if to_find in list_7:
    index=list_7.index(to_find)
    print(f"The element is present in {index} index")
else:
    print("Element not in the list")

#Count the occurrences of an element.
list_8=["hi", "hello", "how", "are", "you","hi","hello"]
print(f"list_8 :{list_8}")

to_count=input("Enter the elements which you want to count the occurance :")

if to_count in list_8:
    print(f"count is : {list_8.count(to_count)}")
else:
    print("Enter element not in the list")

#Sort the list in ascending order.
list_9=[10, 40 , 65 , 33, 21 , 1]
list_9.sort()
print(f"list in ascending order: {list_9}")

#Sort the list in descending order.
list_9=list_9[::-1]
print(f"list in descending order: {list_9}")

#Reverse the list using reverse()
list_9.reverse()
print(f"After reversing list: {list_9}")

a=["Jacintha "]
b=["Christabel"]

#Join two lists using +.
combined_list=a+b
print(f"after joining 2 string : {combined_list}")

#Copy a list.
a=b.copy()
print(f"on copying a to b: {a}")

#Find the maximum element.
list_10=[10, 20, 40 ,8 ,60, 3]
print(f"list_10 is {list_10}")
large=max(list_10)
small=min(list_10)
print(f"maximum element is {large}")
print(f"minimum element is {small}")

