def evaluate_student(name, scores):
    average = sum(scores) / len(scores)
    status = "Passed" if average >= 60 else "Failed"
    print(f"Student: {name}")
    print(f"Average Score: {average:.2f}")
    print(f"Status: {status}\n")

students = [
    ("Alice", [85, 78, 92]),
    ("Bob", [55, 60, 58]),
    ("Charlie", [90, 88, 95]),
    ("Diana", [45, 50, 40]),
    ("Ethan", [70, 65, 72])
]
for student in students:
    name, scores = student
    evaluate_student(name, scores)
