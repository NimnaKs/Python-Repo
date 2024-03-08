x, y, z = 6, 7, 8
print("Many Values to Multiple Variables")
print(f"x : {x}")
print(f"y : {y}")
print(f"z : {z}")

p = q = r = 5
print("One Values to Multiple Variables")
print(f"p : {p}")
print(f"q : {q}")
print(f"r : {r}")

x = y = z = 6, 7, 8
print(f"x : {x}")
print(f"y : {y}")
print(f"z : {z}")

"""
# Output

Many Values to Multiple Variables
x : 6
y : 7
z : 8
One Values to Multiple Variables
p : 5
q : 5
r : 5
x : (6, 7, 8)
y : (6, 7, 8)
z : (6, 7, 8) 
# Return tuple

"""
