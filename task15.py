student_scores = {
    "sasi": 82,
    "kumar": 76,
    "reddy": 87,
    "honey": 94,
    "lucky": 80
}
highest_score_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_score_student]
print("Student name with the highest score:", highest_score_student)
print("Score:", highest_score)
