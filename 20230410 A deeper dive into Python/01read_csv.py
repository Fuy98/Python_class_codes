import csv

with open('students.csv') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)
    for x in pointer:
        score = x[2]
        score = int(score)

        if score >= 9:
             print(x)