# Merge dictionaries in python 3.9 using
# merge (|) and (|=)

# Merging in earlier versions
first_dict = {'orange': 1, 'apples': 2}
second_dict = {'bananas': 3, 'pears': 4}
combined_dict = {**first_dict, **second_dict}
print(combined_dict)
# {'orange': 1, 'apples': 2, 'bananas': 3, 'pears': 4}

# Merging in python 3.9
first_dict = {'orange': 1, 'apples': 2}
second_dict = {'bananas': 3, 'pears': 4}

combined_dict = first_dict | second_dict
print(combined_dict)
# {'orange': 1, 'apples': 2, 'bananas': 3, 'pears': 4}
