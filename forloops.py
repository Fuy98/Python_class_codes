# %%/
# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-----------------------------------------")

# %%
# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 10, 2):
    print(x)

print("----------------------------------------")
# %%
# Iterate through letters in a string
word = "Peace"
for z in word:
    print(z)
# %%
print("----------------------------------------")

# %% Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)

print("----------------------------------------")
# %%
# Loop while a condition is being met
run = "y"

while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y': ")

# %%
# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)

# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
for word in words:
    print(word)

# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes" 
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")