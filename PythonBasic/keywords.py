'''
In Python, keywords are reserved words that
have a special meaning and cannot be used as
identifiers (names for variables, functions,
classes, etc.).

These keywords define the
syntax and structure of the Python language.
Here is the list of Python keywords:

False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise


These keywords are case-sensitive, so `True` and `true` would be treated differently.

'''

import keyword

keyword_list = keyword.kwlist
print(f"Keywords of python is : {keyword_list}")

