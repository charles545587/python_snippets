# Return a boolean match to the start or end of a string
# Use the startswith() or endswith() method
# Provided by Charles Roberts (achrober)

some_example_string = 'foobar'

some_example_string.startswith('foo')  # returns True

some_example_string.endswith('bar')  # returns True

# Example 1 perform a match on a file extension
my_template = '~/documents/cfn_template.json'
if my_template.endswith('.json'):
    print('The file is json')  # prints "The file is json"

# Example 2 perform a match on an s3 url
my_s3_url = 's3://my-example-bucket/cfn_template.json'
if my_s3_url.startswith('s3://'):
    print('The file is in an s3 bucket')
    # prints "The file is in an s3 bucket"
