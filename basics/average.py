# .split() cuts the text by spaces, and map() converts each piece into an integer
a, b, c = map(int, input("Enter 3 numbers separated by spaces: ").split())    #take multiple inputs for user

avg=(a+b+c)/3              # / gives a float (decimal result)
avg_1=(a+b+c)//3           # // gives an int (drops decimal)

print(f"average of 3 numbers with decimal is {avg}")
print(f"average of 3 numbers without decimal is {avg_1}")
