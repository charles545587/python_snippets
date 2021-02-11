# Using Try, Except, Finally and Else clauses 
# handle errors and exceptions gracefully
# comment out examples as required so they run

# Test 1 - Generating a single error, change number1 to zero
# Test 2 - Adding a second error type, change number1 to 'apple'
# Test 3 - Use an 'else' clause if no error is generated, change number 1 to 2
# Test 4 - Use a 'finally' clause to run if the code is sucessful or generates an error 
number = 2
number1 = 2

# handling a single error
try:
    print(f'The outcome of the sum was: {number / number1}')
except ZeroDivisionError as error:
    print(f'You attempted to divide by zero this raised an {error=}')


# handling multple error types 
try:
    print(f'The outcome of the sum is: {number / number1}')
except ZeroDivisionError as error:
    print(f'You attempted to divide by zero this raised an {error=}')
except TypeError as error:
    print(
        f'You attemed to divide an integer '
        f'by a string which raised an {error=}')

# Using an else clause to run code if no exception is raised.
try: 
    print(f'The outcome of the sum is: {number / number1}')
except ZeroDivisionError as error:
    print(f'You attempted to divide by zero, this raised an {error=}')
else:
    print('Your sum was a sucess and did not raise an error, congratulations')

# Using 'finally' to run code irrespective of success or error being generated
try:
    print(f'The outcome of the sum is: {number / number1}')
except ZeroDivisionError as error:
    print(f'You attemed to divide by zero, this raised an {error=}')
finally:
    print(
        'This code will run irrespective'
        ' of success or an error being generated')

