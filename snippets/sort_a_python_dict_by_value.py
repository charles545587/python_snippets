# How to sort a Python dict by value

import operator

my_dictionary = {'oranges': 4, 'apples': 3, 'bananas': 2, 'pears': 1}
sorted(my_dictionary.items(), key=operator.itemgetter(1))
print(my_dictionary)

# returns
# {'oranges': 4, 'apples': 3, 'bananas': 2, 'pears': 1}

# or use a lambda function

my_dictionary = {'oranges': 4, 'apples': 3, 'bananas': 2, 'pears': 1}
sorted(my_dictionary.items(), key=lambda x: x[1])
print(my_dictionary)

# returns
# {'oranges': 4, 'apples': 3, 'bananas': 2, 'pears': 1}
