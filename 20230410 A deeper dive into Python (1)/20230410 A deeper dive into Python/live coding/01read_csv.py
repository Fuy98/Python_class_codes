import csv

# NOTE: You can try encoding "Latin1" or "UTF-8" to try to "fix" special characters
with open('students.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)
    for x in pointer:
        score = x[2]
        score = int(score)
        if score>=9:
            print(x)