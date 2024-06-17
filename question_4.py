# Task 1

students = ["John ", "Doe ", "Jane ", "Smith "]
grades = [85, 90, 78, 88]
activities = [" Football", " Music", " Art", " Dance"]

combined = [i + str(j) + k for i, j, k in zip(students, grades, activities)]

bad_students = (students[2], grades[2], activities[2])
print(combined)
print(bad_students)

# Task 2

students_approved = ["John", "Doe", "Smith"]


# Task 3

print(students_approved)
