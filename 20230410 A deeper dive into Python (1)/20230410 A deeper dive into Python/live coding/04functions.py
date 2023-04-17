# Functions: you can think about functions as in a "black bock"

result = round(1.99999, 2)
print(result)

# We are definind a function called "suma"
# this function takes two arguments (a and b)
# and RETURNS the result of a+b
def suma(a,b):
    return a+b

print(suma(5,10))

# Lest do a function that converts from Fahrenheit to Celsius
def f_to_c(f,digits):
    celsius = (f - 32) / 1.8
    celsius = round(celsius, digits)
    return celsius

print(f_to_c(87,4))

july_temperatures = [87,85,92,79,106]
c_temperatures = [f_to_c(x, 4) for x in july_temperatures]
print(c_temperatures)