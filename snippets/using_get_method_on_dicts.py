# The get() method on dicts
# and its "default" argument
# format: variable_name.get(argument, 'default_value')
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


# when get is called it checks if the given key is in the dict.
def greeting(userid):
    return (f"Hi {name_for_userid.get(userid, 'there')}!")

# if the key exists the value is returned.

greeting(382)  #returns "Hi Alice!"

# if it does not exist the value of the default argument is returned.
greeting(333333)  # returns "Hi there!"

# From Real Python

# Useful variation if you want to do a 'deep' get()
# for a nested list when you cannot guarantee that all keys exist:

example = {"foo": {"bar": {"baz": 123}}}
print(example.get("foo", {}).get("bar", {}).get("baz"))  # prints 123
print(example.get("bar", {}).get("foo", {}).get("baz"))  # prints None
