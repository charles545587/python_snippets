# Use os.walk() to list files and directories recursively

import os

# os.walk() returns a generator object
# with a tuple of (dirpath, dirnames, filenames)

# using the current directory
PATH = "."

for dirpath, dirname, filename in os.walk(
    PATH,
    topdown=True,  # Optional defaults to True
    onerror=None,  # Optional defaults to None
    followlinks=False  # Optional default to False
        ):
    for file in filename:
        print(os.path.join(dirpath, file))
    for file in dirname:
        print(os.path.join(dirpath, file))
    if 'site-packages' in dirname:
        dirname.remove('site-packages')  # don't include site-packages


# Documentation https://docs.python.org/3/library/os.html
# Also consider os.fwalk() if you want a file descriptor

