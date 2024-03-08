"""
# In Python, Every variable in Python holds an instance of an object. There are two types of objects in Python i.e.
Mutable and Immutable objects. Whenever an object is instantiated, it is assigned a unique object id. The type of
the object is defined at the runtime and it can’t be changed afterward. However, its state can be changed if it is
a mutable object.

# Mutable Object - int, float, bool, string, Unicode, and tuple

# Immutable object - Mutable Objects are of type Python list, Python dict, or Python set.
Custom classes are generally mutable.

"""

"""
name = "Sahan"
name[1] = "P"
Traceback (most recent call last):
  File "/Users/mac/Desktop/Python/PythonVariables/mutable_vs_immutable.py", line 16, in <module>
    name[1] = "P"
TypeError: 'str' object does not support item assignment

"""

names = ["Nimna", "Kaveesha"]
print(names)
names.insert(2, "Sekara")
print(names)
names.pop(0)
print(names)

my_dict = {"name": "Ram", "age": 25}
new_dict = my_dict
new_dict["age"] = 37

print(my_dict)
print(new_dict)

"""
# Output
{'name': 'Ram', 'age': 37}
{'name': 'Ram', 'age': 37}
"""

my_set = {1, 2, 3}
new_set = my_set
new_set.add(4)

print(my_set)
print(new_set)

"""
# Output
{1, 2, 3, 4}
{1, 2, 3, 4}
"""