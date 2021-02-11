# create a dictionary from two lists using zip()
# More information using help('zip') and help('dict')

# create two lists
dict_keys = ['bananas', 'bread flour', 'cheese', 'milk']
dict_values = [2, 1, 4, 3]

# iterate over lists using zip
iterator_using_zip = zip(dict_keys, dict_values)

# create the dictionary from the zip
dictionary_from_zip = dict(iterator_using_zip)

print(dictionary_from_zip)
# prints {'bananas': 2, 'bread flour': 1, 'cheese': 4, 'milk': 3}
