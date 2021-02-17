# using datetime and timedelta 

import datetime
import time

# create two variables for time with a pause of 5 seconds
time1 = datetime.datetime.now()
time.sleep(5)
time2 = datetime.datetime.now()

# Calcuate the time difference
time_difference = time2 - time1

print(time_difference)
# Returns 0:00:05.003423

print(type(time_difference))
# Returns <class 'datetime.timedelta'>

# datetime.timedelta allows you to make comparisons
if time_difference > datetime.timedelta(seconds=5):
    print(f'This took {time_difference}')
    # Returns 0:00:05.003423

# documentation https://docs.python.org/3/library/datetime.html