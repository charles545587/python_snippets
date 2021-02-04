# Use timeit to measure the time taken to run a snippet of code.
# Possible Use case compare times taken using different methods.
​
import timeit
​
# Two dictionaries for test data
dict1 = {'apple': 1, 'banana': 2, 'cherry': 3}
dict2 = {'dragon fruit': 3, 'eggplant': 3, 'fig': 4}
​
# use timeit to measure time to merge using method supported in 3.6 - 3.8
method_1 = timeit.timeit(lambda: '{**dict1, **dict2}', number=10000)
# use timeit to measure time to merge using method supported in python 3.9
method_2 = timeit.timeit(lambda: 'dict1 | dict2', number=10000)
​
# Return the results
print(f'The time taken for {method_1=}, \nThe time taken for {method_2=}')
# The time taken for method_1=0.0014604240000000018,
# The time taken for method_2=0.0012312010000000012
​
# Compare the results
if method_1 >= method_2:
    print(f'The difference is {method_1 - method_2}')
    print('Method 2 is faster')
else:
    print(f'The difference is {method_2 - method_1}')
    print('Method 1 is faster')
	
# The difference is 0.00022922300000000062
# Method 2 is faster
​
# Documentation https://docs.python.org/3/library/timeit.html
