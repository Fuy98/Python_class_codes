# PYTHON Data Structures

# list
# 1-dimensional collection, index, ordered, mutable

students = ['jose','adrian','frida']

# Dictionary
# Key-paired value data structure
# it doesnt have a index (it has the keys) neither a particular order
# mutable
# the values of the dict can be ANYTHING
actor = {
    'name': 'Sylvester Stallone',
    'age': 62,
    'married': True,
    'best movies': ['Rocky', 'Rocky2', 'Rocky3']
}
# In a dictionary we use the key of the values to extract... the values
# name is the key
# sylvester stallone is the value
print(actor['name'])
print(actor['best movies'][2])

print(f'My favourite movie from {actor["name"]} is {actor["best movies"][0]}')
print(f"My favourite movie from {actor['name']} is {actor['best movies'][0]}")

# Quick note on the f-string template

print('hola' + 'jose') # The + symbols concatenates
print(2+2) # The + symbols make the mathematical operation of addition

#The most "modern" way to concatenate is with the f-string template
new_string = f'The result of 2+2 is {2+2}'
print(new_string)

name = 'jose'
print(f'hello {name}')

