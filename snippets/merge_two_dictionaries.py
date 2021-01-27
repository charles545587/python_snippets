# How to merge two dictionaries
# in python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}

print(z)  # Returns {'a': 1, 'b': 3, 'c': 4}
