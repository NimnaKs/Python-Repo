# i.
sums = 0
for num in range(1, 11):
    sums = sums + num
print(sums)

# ii.
add = 0
for num in range(100, 1, -25):
    add = add + num
print(add)

# iii.
a = b = 2
# a = 2 , b = 2
c, d = -5, "Saman"
# c = -5 ,d = Saman
print('a=', a, 'b=', b, 'c=', c, 'd=', d)
#

print(bin(25))
print(hex(25))
print(oct(25))

print(chr(97), ord('A'))

var_string = "Hello World"
print(var_string[::-1])

try:
    num1 = 10 / 0
except:
    print("Hello")

lst1 = [11, 12, 13, 14, 15, 16, 17]
lst2 = lst1
lst3 = [11, 12, 13, 14, 15, 16, 17]

lst1[-1: -3: -1] = [18, 19]

print(lst1)
# [18, 19, 15, 16, 17]
print(lst2)
# [18, 19, 15, 16, 17]
print(lst3)
# [11, 12, 13, 14, 15, 16, 17]

print(id(lst1))
# same
print(id(lst2))
# same
print(id(lst3))
# not same

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])