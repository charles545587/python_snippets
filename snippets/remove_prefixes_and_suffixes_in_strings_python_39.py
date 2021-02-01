# Remove prefixes and suffixes from strings in python 3.9
# Introduced by pep 616

my_string = "The quick brown fox jumped over the lazy dog"

print(my_string.removeprefix('The'))
# Returns: quick brown fox jumped over the lazy dog

print(my_string.removesuffix('dog'))
# Returns: The quick brown fox jumped over the lazy

