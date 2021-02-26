# Extract docstrings from python using ast

import ast


def load_source_code(source_filename=__file__):
    """
    Open a script to parse.
​
    :param source_filename: Full path to script to parse, if not provided,
                            this script will parse itself.
    :return: Script content as a string
    """
    return open(source_filename, 'r').read()


def get_function_list(source_code):
    """
    Parse the source code using AST and get a list of function objects.
​
    :param source_code: Python source to parse
    :return: List of function objects from source
    """
    source_tree = ast.parse(source_code)
    return (i for i in source_tree.body if isinstance(i, ast.FunctionDef))


def get_function_details(functions):
    """
    Create a generator for function name/docstring tuples.
​
    :param functions: Iterable of function objects from source code
    :return: Generator of tuples of fuction names and docstrings
    """
    return ((f.name, ast.get_docstring(f)) for f in functions)


source_code = load_source_code()
functions = get_function_list(source_code)
function_details = get_function_details(functions)

for name, docstring in function_details:
    print(name)
    print('-' * len(name))
    print(docstring)
    print()
