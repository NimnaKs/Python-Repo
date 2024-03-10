a = b = 5, 4  # a = 5,4 b=5,4

c, d, e = 2, 5, -4  # c = 2 , d = 5 , e = -4

print("a:", a, "d:", d, "e:", e)

# a: (5,4) d: 5 e : -4

if c > d:
    # 2 > 5 - false
    print("I am a Orange")
else:
    print("I am an Apple")

# I am an Apple

mylist = "Hola!"  # Collection of sequence of characters H + o + l + a+ !
newlist = set(mylist)
print(newlist)

# {'l', 'o', 'H', 'a', '!'}

for a in mylist:
    print(a)
    # H
    # o
    # l
    # a
    # !

print(mylist[-1])
# H o l a !
# 0 1 2 3 4
# -5  -4  -3  -2  -1

# !

print(mylist[0])

# H

print(mylist[2:])
# slice [starting index , end index , steps]

#l a !

print(mylist[:5])

# Hola!

a = {'a', 'b', 'c'}
b = {'a', 'e'}

print(a.intersection(b))
# Comman - a & b
# {a}

print(a - b)

# {b,c}

