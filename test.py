my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing
print(my_list[-3:0:-2])

# unpacking
a, b, c = 1, 2, 3

d, e = 4, 5

value1 = 10
value2 = 20

# Swapping using unpacking
value2, value1 = value1, value2
print(value1, value2)

# String methods and transformations.
text = "Hello, World!"

print(list(text))
print(tuple(text))

data = '1,2,3,4,5,6,7,8,9,10'

print(data.split())

print(''.join(data.split(',')) + ''.join(tuple(text)))

hello, world = "Hello World".split(' ')
print(hello, world)

scrambled = ''.join(list(hello) + list(world))
print(scrambled)

# Dictionary
my_dict = {'name': 'John', 'age': 25, 'job': 'Programmer'}
print(tuple(my_dict))
print(len(my_dict))
print(my_dict.items())
print(tuple(my_dict.values()))
print(my_dict.get('name'))
print(my_dict['name'])
