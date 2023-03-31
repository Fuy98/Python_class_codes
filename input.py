# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "What is your classmate name?"
name1 = input("What is your classmate name? ")

# Collects the user's input for the prompt "How many months have you been coding?" and converts the string to an integer.
age = int(input("How many months have you been coding? "))

# Collects the user's input for the prompt "How many months have you been coding?" and converts the string to an integer.
age1 = int(input("How many months have you been coding? "))

total = age + age1 

print("My name is " + str(name) + " and I have been coding for " + str(age) + " months.")
print("Their name is " + str(name1) + " and they have been coding for " + str(age1) + " months.")

print("And we have been coding for " + str(total) + " months")