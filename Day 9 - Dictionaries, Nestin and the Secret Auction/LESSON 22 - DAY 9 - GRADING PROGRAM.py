student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {
}
# TODO-2: Write your code below to add the grades to student_grades.👇
"""for students in student_scores:
  student_grades[students] = student_scores[students]
  if student_grades[students] <= 100 and student_grades[students] >= 91:
    student_grades[students] = "Outstanding"
  elif student_grades[students] <= 90 and student_grades[students] >= 81:
    student_grades[students] = "Exceeds Expectations"
  elif student_grades[students] <= 80 and student_grades[students] >= 71:
    student_grades[students] = "Acceptable"
  else:
    student_grades[students] = "Fail"""
# Actually, there's a more efficient way to do this
for students in student_scores:
    score = student_scores[students]
    if score > 90:
        student_grades[students] = "Outstanding"
    elif score > 80:
        student_grades[students] = "Exceeds Expectations"
    elif score > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
print(student_scores)
"""
Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione
"""