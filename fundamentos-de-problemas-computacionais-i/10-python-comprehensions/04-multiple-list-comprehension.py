# Flattening a matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)

# Comprehension
flattened = [num for row in matrix for num in row]
print(flattened)
