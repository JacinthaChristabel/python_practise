#Create a dictionary to store a student's name, age, and marks
s1={
    "name" : "hema",
    "age":9,
    "mark":90
}

#Print the entire dictionary
print(s1)

#Access the value of a specific key
print(f"student age is {s1["age"]}")

#Add a new key-value pair
s1["subject"]="English"
s1.update({"city": "Mysuru"})
s1.update({"class":"3"})
print(s1)

#Update the value of an existing key
s1["age"]=10
print(s1)

#Remove a key using pop()
s1.pop("name")
print(s1)

#Remove the last inserted item using popitem()
s1.popitem()
print(s1)

#Delete a key using del
del s1["subject"]
print(s1)

#Find the number of key-value pairs
print(f"Number of key-value pairs: {len(s1)}")

#Check whether a key exists in the dictionary
if("age" in s1):
    print(f"age is present {s1['age']}")
else:
    print("not present")

print(f"age in s1 : {"mark" in s1}")

