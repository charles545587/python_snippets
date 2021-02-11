# How to merge two dictionaries using **
# in python 3.5+

first_dict = {'orange': 1, 'apples': 2}
second_dict = {'bananas': 3, 'pears': 4}
combined_dict = {**first_dict, **second_dict}

print(combined_dict)
# {'orange': 1, 'apples': 2, 'bananas': 3, 'pears': 4}
