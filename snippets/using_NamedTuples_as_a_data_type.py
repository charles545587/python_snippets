# Use namedTuples to create more readable, self-documenting code
# They can be used wherever regular tuples are used,
# and they add the ability to access fields by name instead of position index.

from collections import namedtuple

user_record = namedtuple('user_record', [
    'first_name',
    'last_name',
    ])

first_user = user_record('John', 'Doe')
second_user = user_record('Ada', 'Lovelace')

# can use numerical indexing like a tuple
print(f'Hello {first_user[0]} {first_user[1]}, how are you?')
# Response: Hello John Doe, how are you?

# can use a named field for more readable code
print(f'Hello {second_user.first_name} {second_user.last_name}, how are you?')
# Response: Hello Ada Lovelace, how are you?

# Can be iterated
for i in first_user:
    print(i)
# Response:
# John
# Doe

# https://docs.python.org/3/library/collections.html#collections.namedtuple
