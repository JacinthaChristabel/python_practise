
# Accept user inputs from the console
name=input("Enter your name: ")
age=int(input("Enter your age: "))  # Read as string, then cast it to an integer
city=input("Enter your city: ")

print("*"*10)           # Print a visual top border using string repetition
# formatted string literals (f-strings)
print(f"You entered name as {name}")
print(f"You entered age as {age}")
print(f"You entered city as {city}")

print("*"*10)            # Print a visual bottom border using string repetition