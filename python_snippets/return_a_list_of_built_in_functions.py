# Return a list of built in python functions
import builtins
import types

builtin_function_names = [name for name, obj in vars(builtins).items()
                          if isinstance(obj, types.BuiltinFunctionType)]
for item in builtin_function_names:
    print(item)


"""
__build_class__
__import__
abs
all
any
ascii
bin
breakpoint
callable
chr
compile
delattr
dir
divmod
eval
exec
format
getattr
globals
hasattr
hash
hex
id
input
isinstance
issubclass
iter
len
locals
max
min
next
oct
ord
pow
print
repr
round
setattr
sorted
sum
vars
open
"""