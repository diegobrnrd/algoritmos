# Strings that start with "a" and end in "y"
options = ['any', 'albany', 'apple', 'world', 'hello', '']
valid_string = []

for string in options:
    if len(string) <= 1:
        continue
    if string[0] != 'a':
        continue
    if string[-1] != 'y':
        continue
    valid_string.append(string)

print(valid_string)

# Comprehension
valid_string = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == 'a'
    if string[-1] == 'y'
]

print(valid_string)
