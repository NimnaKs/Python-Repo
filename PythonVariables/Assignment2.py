# Activity 01

number = 6
# Integer
print(type(number))

name = "UCSC"
# String
print(type(name))

gpa = 3.5
# Float
print(type(gpa))

x = 8
# Integer
print(type(x))

result = number > x
# Boolean
print(type(result))

average = 5.333
# Float
print(type(average))

y = 3.5 + 4.4j
# Complex
print(type(y))

# Activity 02

original_string = "Python is awesome !"
print(f"Length of the String : {len(original_string)}")
print(f"String to lower case : {original_string.lower()}")

# Activity 03

my_list = ["Nimna", 22, 69.89]
print(f"Length of the list : {len(my_list)}")
my_list.append(2 + 2j)
print(f"my_list : {my_list}")
my_list.remove("Nimna")
print(f"my_list : {my_list}")

# Activity 04

my_dict = {"name": "Nimna", "age": 22, "program": "GDSE"}
print(f"Keys = {my_dict.keys()}")
print(f"Values = {my_dict.values()}")
my_dict["Batch"] = 65
print(f"Dictionary after adding new key-value : {my_dict}")
del my_dict["name"]
print(f"Dictionary after removing key-value : {my_dict}")
my_dict["age"] = 23
print(f"Dictionary after updating key-value : {my_dict}")

# Activity 05

name = input("Enter your name : ")
print(f"Hello {name} ! How are you ? ")

# Activity 06

fname = input("Enter  user first name : ")
lname = input("Enter user last name : ")

print(f"{lname} {fname}")
