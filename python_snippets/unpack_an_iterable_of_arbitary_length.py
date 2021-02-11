# Unpack a list of arbitary length using 'star expressions'

my_shoppling = ('fruit', 'apples', 'bananas', 'cherries')

# Use the star expression to unpack the list
category, *list_of_fruits = my_shoppling
print(category, list_of_fruits)
# Returns fruit ['apples', 'bananas', 'cherries']
# The star expression creates a list from the unpacked elements

# Create a dictionary from the returned objects
my_shopping = dict({category: list_of_fruits})
print(my_shopping)
# Returns {'fruit': ['apples', 'bananas', 'cherries']}

