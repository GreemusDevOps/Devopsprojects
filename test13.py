student_scores = {'sasi': 95,'manu': 94,'bindu': 88,'anu': 90,'nag': 60}
highest_score_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_score_student]
print("Student with the highest score:", highest_score_student)
print("Score:", highest_score)



