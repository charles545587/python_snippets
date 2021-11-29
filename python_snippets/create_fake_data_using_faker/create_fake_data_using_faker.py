# Create fake data for testing your applications
# https://pypi.org/project/Faker/

from faker import Faker

fake = Faker()

print(fake.name())
# 'Makayla Butler'

print(fake.first_name())
# Danielle


print(fake.address())
# '1336 Sean Hollow'
# 'North Michael, NC 09926'


# create a list of 10 first names using a list comprehension
# print the list using enumerate for the index value and start at number 1
names = [fake.first_name() for _ in range(10)]
for i, name in enumerate(names, start=1):
    print(i, name)


