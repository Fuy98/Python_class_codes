
# List comprehensions

# List
scores = [8,9,10]

# What if we want to scale this scores from 0 to 100
# i.e. multiply each score by 10
# To do this we need to iterate...

new_scores = []
for x in scores:
    new_scores.append(x*10)

print(new_scores)

# A list comprehension is a short-handed version
# of a for-loop that generates a new list...
# new variable = [return value, iterator, iterable]
new_scores = [x*10 for x in scores]
print(new_scores)


# Activity
# Convert this F temperatures fo C
july_temperatures = [87,85,92,79,106]

# Create the new list with the C temperatures

# 87 F is 30.55 C
c_temperatures = [round((x - 32) / 1.8,2) for x in july_temperatures]
print(c_temperatures)

# FUNCTIONS


