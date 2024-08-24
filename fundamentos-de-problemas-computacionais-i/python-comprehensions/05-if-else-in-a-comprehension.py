# Categorize numbers as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append('Even')
    else:
        categories.append('Odd')

print(categories)

# Comprehension
categories = [
    'Even' if x % 2 == 0 else 'Odd' for x in range(10)
]

print(categories)
