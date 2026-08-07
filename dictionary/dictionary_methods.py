student = {
    "name": "hema",
    "age": 10,
    "mark": 90
}

#Print all keys
print(student.keys())
#Print all values
print(student.values())

#or 

for i in student.keys():    #prints keys in new line
    print(i)

for i in student.values():
    print(i)

#Print all key-value pairs
print(student)
print(student.items())

# Alternatively, using a loop:
for key, value in student.items():
    print(f"{key}: {value}")

#Convert dictionay to list
print(list(student.keys()))
print(list(student.values()))

# Copy a dictionary
s2=student.copy()
print(s2)

# Clear a dictionary
s2.clear()
print(s2)

# Create a dictionary using dict()
s1=dict(name="me",age=10)
print(s1)

# Create a dictionary using fromkeys().
#fromkeys() creates a new dictionary with specified keys and sets a default value for all of them

key=["name","class"]
default_value=None
s3=dict.fromkeys(key, default_value)
print(s3)

# Get the value of a key using get()

print(student.get("age"))         # Fetching an existing key using get
print(student.get("grade", "Not Found"))  # Fetching a non-existing key (returns default message instead of Error)


# Use setdefault() to add a key if it doesn't exist
s4 = {"name": "hema", "age": 10}

s4.setdefault("mark", 90)                 # Key "mark" doesn't exist, so it gets added with value 90
s4.setdefault("age", 15)                  # Key "age" already exists, so its value remains unchanged

print(s4)


# Merge two dictionaries
dict1 = {"name": "hema", "age": 10}
dict2 = {"mark": 90, "city": "Mysuru"}

# Method 1: Using the | operator (Python 3.9+)
merged_dict = dict1 | dict2
print(merged_dict)

# Method 2: Using update()
dict1.update(dict2)
print(dict1)
