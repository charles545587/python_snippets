# Python 3 code to demonstrate the
# use of hashlib to generate hashes
# hashes available:
#   SHA1, SHA224, SHA256, SHA384, SHA512,
#   SHA384, MD5, blake2b, blake2s

import hashlib

# Creates the hash
first_value_to_hash = hashlib.sha256()
first_value_to_hash.update(b"The quick brown fox jumps over the lazy dog.")

# Produces the output using hexidecimal characters.
first_result = first_value_to_hash.hexdigest()

# Second example
second_value_to_hash = hashlib.sha256()
second_value_to_hash.update(b"the quick brown fox jumps over the lazy dog.")
second_result = second_value_to_hash.hexdigest()

# Compare the strings of the hash values
compare_hashes = (first_result == second_result)
if compare_hashes is True:
    print('The hashes match')
else:
    print(
    f"""
    The hashes do not match: \n
    {first_result}, \n
    {second_result}, \n
    """
    )
