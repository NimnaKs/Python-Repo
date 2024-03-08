# Text type - String
var_str = "Hello World"
print(f"var_str : {var_str} : {type(var_str)}\n")

# Numeric type - Integer , Float, Complex
var_int = 10
var_float = 0.5
var_complex = 1 + 1j
print(f"var_int : {var_int} : {type(var_int)}\n"
      f"var_float : {var_float} : {type(var_float)}\n"
      f"var_complex : {var_complex} : {type(var_complex)}\n")

# Sequence type - List,Tuple,Range
var_list = ["Red", 1, 1 + 1j, 0.5]
var_tuple = ("Red", 1, 1 + 1j, 0.5)
var_range = range(10)
print(f"var_list : {var_list} : {type(var_list)}\n"
      f"var_map : {var_tuple} : {type(var_tuple)}\n"
      f"var_range : {var_range} : {type(var_range)}\n")

# Map type - Dictionary,Set,Frozenset
var_dict = {"name": "Nimna", "age": 20, "fav_colors": ["Red", "Yellow", "Orange"]}
var_set = {"Nimna", 20, 1 + 1j}
var_frozenSet = frozenset({"Nimna", 20, 1 + 1j})
print(f"var_dictionary : {var_dict} : {type(var_dict)}\n"
      f"var_set : {var_set} : {type(var_set)}\n"
      f"var_frozenset : {var_frozenSet} : {type(var_frozenSet)}\n")

# Boolean type
var_boolean = True
print(f"var_boolean : {var_boolean} : {type(var_boolean)}\n")

# None type
var_none = None
print(f"var_none : {var_none} : {type(var_none)}\n")

# Binary type
var_bytes = b"Hello"
var_bytearray = bytearray(5)
var_memoryview = memoryview(bytes(5))
print(f"var_bytes : {var_bytes} : {type(var_bytes)}\n"
      f"var_bytearray : {var_bytearray} : {type(var_bytearray)}\n"
      f"var_memoryview : {var_memoryview} : {type(var_memoryview)}\n")
