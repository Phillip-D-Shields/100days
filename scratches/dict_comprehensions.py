# new_dict = {new_key: new_value for {key,value} in dict.items()}
import random

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
students_scores = {student:random.randint(60,101) for student in names}

print(students_scores)

passed_students = {student:score for student, score in students_scores.items() if score > 70}
print(passed_students)