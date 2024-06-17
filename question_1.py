#Task1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)

print(grades)

#Task2

def average(grades):
    return sum(grades) / len(grades)


print(average(grades))

#Task3

new_value = "Failed"

replace_grades = [new_value if grade < 80 else grade for grade in grades]

print(replace_grades)
