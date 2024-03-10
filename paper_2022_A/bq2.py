var_input = input("Enter number of elements in the list : ")
# "5"

var_int_input = int(var_input)

my_list = []

for i in range(0, var_int_input):
    num = int(input(f"Enter element No {i + 1} : \n"))
    my_list.append(num)

print(f"The entered list is:\n {my_list}")

print(f"Average = {sum(my_list)/var_int_input} No. elements = {var_int_input}")


