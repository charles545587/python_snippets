# create a dictionary from two unequal lists using zip_longest
# and dict
import itertools

my_short_list = ['oranges', 'carrots', 'peas']
my_long_list = ['first_item', 'second_item', 'third_item', 'fourth_item']

dictionary_from_zip_longest = dict(
    itertools.zip_longest(my_long_list, my_short_list, fillvalue=None))
print(dictionary_from_zip_longest)
# Response
# {'first_item': 'oranges',
#  'second_item': 'carrots',
#  'third_item': 'peas',
#  'fourth_item': None}
