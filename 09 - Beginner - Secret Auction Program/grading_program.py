student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}
student_grades = {}

for key, value in student_scores.items():
    print(key, value)
    if value > 90:
        student_grades[key] = "Outstanding"
    elif 80 < value < 91:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < value < 81:
        student_grades[key] = "Acceptable"
    elif value < 71:
        student_grades[key] = "Fail"

for key, value in student_grades.items():
    print(key, value)
