# Unpack an iterable of arbitary length using 'star expressions'

my_shopping = ("fruit", "apples", "bananas", "cherries")

# Use the star expression to unpack the elements
category, *list_of_fruits = my_shopping
print(category, list_of_fruits)
# Returns fruit ['apples', 'bananas', 'cherries']
# The star expression creates a list from the unpacked elements

# Create a dictionary from the returned objects
my_shopping_dict = dict({category: list_of_fruits})
print(my_shopping_dict)
# Returns {'fruit': ['apples', 'bananas', 'cherries']}

