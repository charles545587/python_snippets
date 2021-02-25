# Problem

# Python uses the built in json library to convert a dict to json
# the dict contains datetime dataformat which is not supported by json

import datetime
import json

example_dictionary = dict([('date', datetime.datetime.now())])

# Returns {'date': datetime.datetime(2021, 2, 17, 10, 17, 4, 575133)}

convert_to_json = json.dumps(example_dictionary, indent=4)
# Generates a TypeError: Object of type datetime is not JSON serializable
# Reason json does not support the datetime data format

# Solution

# Convert the datetime to a string using the default=str keyword parameter
convert_to_json = json.dumps(example_dictionary, indent=4, default=str)

print(convert_to_json)
# Returns
# {
#     "date": "2021-02-17 10:24:09.146207"
# }

# Alternative solution - use an f-string to evaluate datetime
example_dictionary = dict([('date', f'{datetime.datetime.now()}')])
