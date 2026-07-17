#find common elements in 2 list
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]

# Convert to sets and find the intersection
common_elements = list(set(list_1) & set(list_2))

print(common_elements)  # Output: [4, 5]