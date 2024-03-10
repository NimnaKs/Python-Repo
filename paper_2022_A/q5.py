a = {1, 2, 3}  # Set c={1,2,3} d={1,2,3,4}
b = {3, 4, 2}  # Set
print(a.isdisjoint(b)) #False
print(a & b) # {2,3}
print(a - b) # {1}
print(a^b) # {1,4}
