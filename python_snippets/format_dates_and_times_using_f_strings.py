# Format dates and times using f-strings

import datetime
date = datetime.datetime.now()

print(date)  # prints datetime.datetime(2021, 1, 22, 13, 42, 36. 875142)

# Use the f-string to format the date
print(f"{date:%Y-%m-%d}")  # prints 2021-01-2
