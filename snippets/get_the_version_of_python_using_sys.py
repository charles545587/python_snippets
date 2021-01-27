# Get the version of python at runtime using sys
import sys

version = sys.version
print(version)
# returns '3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53)
#  \n[Clang 6.0 (clang-600.0.57)]'

# Test for minimum version of python at runtime
if not sys.version_info >= (3, 5):
    sys.exit('version of python must be 3.5 or greater')
    # returns version of python must be 3.5 or greater
else:
    pass
