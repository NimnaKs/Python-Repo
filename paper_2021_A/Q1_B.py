my_dict = {'Name': 'Annie', 'Age': '5', 'Class': 'First', 'Address': 'Colombo', 'Height': '1.2', 'School': 'Primary',
           'Gender': 'Female'}

# 1 .
print(my_dict)

# 2 .
if 'School' in my_dict:
    print('Yes! Key School is in my dict')
else:
    print('No! Key School is not in my dict')

# 3 .
my_dict['Age'] = '7'

# 4 .
del my_dict['Height']

# 5.
print(my_dict)
