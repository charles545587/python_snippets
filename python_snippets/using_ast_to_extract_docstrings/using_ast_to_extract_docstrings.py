# Using AST to extract docstrings from python.

# create a separate file called example_function.py
# create a function with a docstring in example_function.py
# for example:
# def my_example_function():
#     """
#     This is an example docstring
#     """
import os
import ast
import json

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, "example_function.py")

with open(file_path, 'r') as f:
    file_contents = f.read()

# ast will parse a string, confirm that the opened file is a string
print(type(file_contents))

# parse the file using ast
parsed_file = ast.parse(file_contents)

# extract the functions from the parsed file using ast.FunctionDef
# using a list comprehension
list_of_function_definitions = (
    [function for function in parsed_file.body
        if isinstance(function, ast.FunctionDef)])

# Generate a list of the function names using a list comprehension
function_names = [function.name for function in list_of_function_definitions]

# Use the ast.get_docstring on an ast.FunctionDef object
for function in list_of_function_definitions:
    function_name = function.name
    docstring = ast.get_docstring(function)

    print(function_name + ": " +  docstring)

# With lots of help from https://gabrielelanaro.github.io/blog/2014/12/12/extract-docstrings.html