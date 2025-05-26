def average_score(student: list[list], scores: list) -> str:
    average = sum(scores) / len(scores)
    for students in student:
        if average >= 60:
            print(f'Mr/Mrs {student}, you have passed the exam with an average score of: {average}')