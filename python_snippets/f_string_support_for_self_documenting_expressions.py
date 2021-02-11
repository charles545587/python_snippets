# Use the '=' in an f-string to include the expression in the result returned
# Introduced in python 3.8

first_name = 'John'
family_name = 'Doe'

# Using the f-string without '=' returns just the value of the variable 
print(f'Hello {first_name} {family_name}!')

# Returns "Hello John Doe!"

# use the '=' to return the variable name and the value
print(f'The values entered were {first_name=} and {family_name=}')
# Returns "The values entered were first_name='John' and family_name='Doe'"
