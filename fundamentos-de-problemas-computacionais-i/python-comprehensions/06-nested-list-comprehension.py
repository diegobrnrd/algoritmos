# Building a 3D list
import pprint
printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)

printer.pprint(lst)

# Comprehension
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst)
